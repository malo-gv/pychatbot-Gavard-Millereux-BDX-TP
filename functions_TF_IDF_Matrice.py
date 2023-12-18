import os
import string


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
                nom_fichier = filename

                # Calculer le score TF pour le mot dans le document
                tf = calculer_tf(nom_fichier).get(mot, 0)

                # Calculer le score TF-IDF en multipliant le score TF par le score IDF
                tfidf = tf * idf.get(mot, 0)

                # Ajouter le score TF-IDF au vecteur
                vecteur.append(tfidf)

        # Ajouter le mot et son vecteur TF-IDF à la liste
        matrice.append(vecteur)

    return matrice


# Fonction pour calculer la transposée d'une matrice
def calculer_transposee(matrice):
    # On échange les lignes et les colonnes
    return [[matrice[j][i] for j in range(len(matrice))] for i in range(len(matrice[0]))]


from functions_TF_IDF_Matrice import calculer_tf, calculer_idf


def calculer_vecteur_tf_idf_question(question, directory):
    liste_mots_question = tokeniser_question(question)

    tf_question = {}
    for mot in liste_mots_question:
        tf_question[mot] = liste_mots_question.count(mot) / len(liste_mots_question)

    idf_corpus = calculer_idf(directory)
    vecteur_tfidf_question = []
    for mot in liste_mots_question:
        tfidf_score = tf_question.get(mot, 0) * idf_corpus.get(mot, 0)
        vecteur_tfidf_question.append(tfidf_score)

    return vecteur_tfidf_question


import math


def vecteur(A, B):
    return sum(a * b for a, b in zip(A, B))


def vector_norm(A):
    return math.sqrt(sum(a * a for a in A))


def similarite(A, B):
    result = vecteur(A, B)
    norm_A = vector_norm(A)
    norm_B = vector_norm(B)

    # Vérifiez si l'un des vecteurs a une norme nulle
    if norm_A == 0 or norm_B == 0:
        return 0  # Évitez la division par zéro en renvoyant 0

    # Assurez-vous que la similarité est dans la plage [0, 1]
    similarity = max(0, min(result / (norm_A * norm_B), 1))
    return similarity


def document_pertinent(tfidf_corpus, tfidf_question):
    document_names = os.listdir('ressources/cleaned')
    max_similarity = -1
    i = 0
    most_similar_document_name = None

    for elt in tfidf_corpus:
        similarity = similarite(elt, tfidf_question)

        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_document_name = document_names[i]
        while i <= len(tfidf_corpus):
            i = i + 1
    return most_similar_document_name


def tokeniser_question(question):
    contenu_sans_ponctuation = ''.join(
        caractere if caractere not in string.punctuation else ' ' for caractere in question)
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
    mots = contenu_final.split()
    return mots

def rechercher_mot_quest(liste_mots, mots_corpus):
    liste_inter = []
    for mot in liste_mots:
        if mot in mots_corpus :
            liste_inter.append(mot)
    return liste_inter
