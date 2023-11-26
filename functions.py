# Import des fonctions autres

import os
import math
import string


def list_of_files(directory, extension):  # Met les noms des fichiers dans une liste
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def donner_nom(nom_fichier):  # Récupération du nom du président

    nom_president = ""
    for i in range(11, len(nom_fichier)):
        nom_president = nom_president + nom_fichier[i]
        if (nom_fichier[i + 1] == ".") or (nom_fichier[i + 1] >= '0' and nom_fichier[i + 1] <= '9'):
            # On arrête la récupération avant le "." ou un chiffre
            return nom_president


def donner_prenom(nom_president):
    prenom_pre = ""

    if nom_president == "Chirac":
        prenom_pre = "Jacques"

    if nom_president == "Giscard dEstaing":
        prenom_pre = "Valery"

    if nom_president == "Hollande":
        prenom_pre = "François"

    if nom_president == "Mitterrand":
        prenom_pre = "François"

    if nom_president == "Macron":
        prenom_pre = "Emmanuel"

    if nom_president == "Sarkozy":
        prenom_pre = "Nicolas"

    return prenom_pre


def copier_texte(nom_fichier):
    contenu_fichier = ""
    with open(nom_fichier, 'r', encoding='utf8') as fichier:
        contenu_fichier = fichier.read()
    return contenu_fichier


def convertir_en_minuscules(contenu_fichier):
    contenu_minus = contenu_fichier.lower()
    return contenu_minus


def transferer_contenu(contenu_minus, nom_fichier):
    nom_desti = nom_fichier
    if not os.path.exists("./ressources/cleaned"):
        os.mkdir("./ressources/cleaned")  # On crée un répertoire cleaned
    if not os.path.exists("./ressources/cleaned/nom_desti"):
        with open("./ressources/cleaned/" + nom_desti, 'w', encoding='utf8') as fichier_destination:
            fichier_destination.write(contenu_minus)  # On crée un fichier texte en minuscule dans le répertoire cleaned
    fichier_destination.close()


def nettoyer_texte(nom_fichier):
    chemin_fichier = "./ressources/cleaned/" + nom_fichier
    with open(chemin_fichier, 'r', encoding='utf8') as fichier:
        contenu = fichier.read()
    contenu_sans_ponctuation = ''.join(
        caractere if caractere not in string.punctuation else ' ' for caractere in contenu)
    contenu_traite = []
    mots = contenu_sans_ponctuation.split()
    for mot in mots:
        if '-' in mot:
            sous_mots = mot.split('-')
            contenu_traite.extend(sous_mots)
        elif "'" in mot:
            sous_mots = mot.split("'")
            contenu_traite.extend(sous_mots)
        else:
            contenu_traite.append(mot)
    contenu_final = ' '.join(contenu_traite)
    with open(chemin_fichier, 'w', encoding='utf8') as fichier_destination:
        fichier_destination.write(contenu_final)


def calculer_tf(nom_fichier):
    chemin_fichier = "./ressources/cleaned/" + nom_fichier
    with open(chemin_fichier, 'r', encoding='utf8') as fichier:
        texte = fichier.read()

    mots = texte.split()
    frequence = {}

    for mot in mots:
        frequence[mot] = frequence.get(mot, 0) + 1
    return frequence


# Fonction pour calculer le score IDF dans l'ensemble du corpus en utilisant TF-IDF
def calculer_idf(directory):
    nombre_documents = 0
    idf = {}

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # Assurez-vous que les fichiers ont l'extension .txt
            nombre_documents += 1
            chemin_fichier = os.path.join(directory, filename)
            with open(chemin_fichier, 'r', encoding='utf8') as fichier:
                contenu = fichier.read()
            mots_uniques = set(contenu.split())

            for mot in mots_uniques:
                idf[mot] = idf.get(mot, 0) + 1

    for mot, nombre_apparitions in idf.items():
        idf[mot] = math.log(nombre_documents / (1 + nombre_apparitions))  # On ajoute 1 pour ne pas diviser par 0

    return idf


def generer_matrice(directory):
    mots_uniques = set()

    # Construire un ensemble de tous les mots uniques dans le corpus
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            chemin_fichier = os.path.join(directory, filename)
            with open(chemin_fichier, 'r', encoding='utf8') as fichier:
                contenu = fichier.read()
            mots_uniques.update(set(contenu.split()))

    idf = calculer_idf(directory)

    matrice = []

    # Pour chaque mot unique, construire son vecteur TF-IDF
    for mot in mots_uniques:
        vecteur = []

        # Pour chaque document, calculer le score TF-IDF du mot
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                nom_fichier = os.path.join(filename)

                # Calculer le score TF pour le mot dans le document
                tf = calculer_tf(nom_fichier).get(mot, 0)

                # Calculer le score TF-IDF en multipliant le score TF par le score IDF
                tfidf = tf * idf[mot]

                # Ajouter le score TF-IDF au vecteur
                vecteur.append(tfidf)

        # Ajouter le vecteur TF-IDF à la matrice
        matrice.append(vecteur)

    return matrice


# Fonction pour calculer la transposée d'une matrice
def calculer_transposee(matrice):
    # On échange les lignes et les colonnes
    return [[matrice[j][i] for j in range(len(matrice))] for i in range(len(matrice[0]))]


def mots_non_importants(directory):
    idf = calculer_idf(directory)
    mots_non_importants = [mot for mot, score_idf in idf.items() if score_idf == 0]
    return(mots_non_importants)


def mot_plus_important(directory):
    matrice = generer_matrice(directory)
    mots_uniques = []

    # Construire une liste de tous les mots uniques dans le corpus
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            chemin_fichier = os.path.join(directory, filename)
            with open(chemin_fichier, 'r', encoding='utf8') as fichier:
                contenu = fichier.read()
            mots_uniques.extend(set(contenu.split()))

    # Construire une liste de tuples (mot_unique, score_tfidf_max)
    mots_score_max = [(mot, max(matrice[mots_uniques.index(mot)])) for mot in mots_uniques]

    # Trouver le mot avec le score TF-IDF le plus élevé
    mot_max = max(mots_score_max, key=lambda x: x[1])

    return mot_max

