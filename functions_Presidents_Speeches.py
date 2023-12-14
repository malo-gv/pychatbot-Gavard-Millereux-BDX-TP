from functions_TF_IDF_Matrice import calculer_idf, calculer_tf, generer_matrice
# Import des fonctions autres
import os
import string
from collections import defaultdict

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


def mots_non_importants(directory):
    idf = calculer_idf(directory)
    mots_non_importants = [mot for mot, score_idf in idf.items() if score_idf == 0] #Les mots non importants ont un IDF de 0
    return (mots_non_importants)


def mot_plus_important(directory):
    matrice = generer_matrice(directory)
    mots_uniques = set()

    # Construire un ensemble de tous les mots uniques (d'où le set) dans le corpus
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            chemin_fichier = os.path.join(directory, filename)
            with open(chemin_fichier, 'r', encoding='utf8') as fichier:
                contenu = fichier.read()
            mots_uniques.update(set(contenu.split()))

    # Construire un dictionnaire pour stocker le score TF-IDF maximal pour chaque mot
    mots_score_max = defaultdict(lambda: 0)

    for mot in mots_uniques:
        index_mot = list(mots_uniques).index(mot) if mot in mots_uniques else -1

        if 0 <= index_mot < len(matrice[0]):
            for i, filename in enumerate(os.listdir(directory)):
                if filename.endswith(".txt"):
                    nom_fichier = os.path.join(directory, filename)
                    if 0 <= i < len(matrice):
                        # Obtenir le score TF-IDF pour le mot dans le document actuel
                        tfidf = matrice[i][index_mot]

                        # Mettre à jour le score TF-IDF maximal pour le mot
                        mots_score_max[mot] = max(mots_score_max[mot], tfidf)

    # Trouver le mot avec le score TF-IDF le plus élevé
    mot_max = max(mots_score_max.items(), key=lambda x: x[1])

    return mot_max


def mots_plus_repetes_par_chirac(directory):
    # On sépare toutes nos étapes en 2 discours
    discours1 = 'Nomination_Chirac1.txt'
    discours2 = 'Nomination_Chirac2.txt'

    freq1 = calculer_tf(discours1)
    freq2 = calculer_tf(discours2)

    mots_uniques_chirac1 = set(freq1.keys())
    mots_uniques_chirac2 = set(freq2.keys())

    tous_mots_uniques = mots_uniques_chirac1.union(mots_uniques_chirac2) #On réunit les deux discours

    freq_globale = {mot: freq1.get(mot, 0) + freq2.get(mot, 0) for mot in tous_mots_uniques} # Pareil pour la fréquence

    mots_plus_repetes = [mot for mot, freq in freq_globale.items() if freq == max(freq_globale.values())]
    return (mots_plus_repetes)


def president_nation(directory):
    mots_freq_nation = {}

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            nom_president = donner_nom(filename)
            mots_freq_nation[nom_president] = calculer_tf(filename).get('nation', 0)

    president_parlant = [president for president, freq in mots_freq_nation.items() if freq > 0] #Si freq > 0 cela signifie que le président a parlé de la nation
    print("Les présidents qui parlent de la nation sont : ",president_parlant)

    president_le_plus = max(mots_freq_nation, key=mots_freq_nation.get) # On prend le maximum parmis tous les présidents en ayant parlé
    print("Le président parlant le plus de la nation est : ",president_le_plus)


def president_ecologie(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            nom_president = donner_nom(filename)
            mots_freq_president = calculer_tf(filename)
            if ("climat" or "écologie" or "ecologie") in mots_freq_president:
                return(nom_president)
                break


def mots_evoques(directory):
    mots_communs = set()
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            mots_president = set(calculer_tf(filename))
            if not mots_communs:
                mots_communs.update(mots_president)
            else:
                mots_communs.intersection_update(mots_president)
    mots_communs = [mot for mot in mots_communs if mot not in mots_non_importants(directory)]
    return(mots_communs)

def recuperer_tout_texte(directory):
    stockage = ""

    for nom_fichier in os.listdir(directory):
        chemin_fichier = os.path.join(directory, nom_fichier)

        if os.path.isfile(chemin_fichier) and nom_fichier.endswith(".txt"):
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                texte_du_fichier = fichier.read()
                stockage += texte_du_fichier
    texte = stockage.split()

    return(texte)


