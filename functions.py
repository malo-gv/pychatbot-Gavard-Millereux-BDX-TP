# Import des fonctions autres

import os
import math
import string


def list_of_files(directory, extension):  # Met les noms des fichiers dans une liste
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    print("On a mit les noms des fichiers dans une liste")
    return files_names

def donner_nom(nom_fichier):  # Récupération du nom du président
    nom_president = ""
    for i in range(11,len(nom_fichier)):
        nom_president = nom_president + nom_fichier[i]
        if (nom_fichier[i+1] == ".") or (nom_fichier[i+1] >= '0' and nom_fichier[i+1] <= '9'):
            # On arrête la récupération avant le "." ou un chiffre
            print("On a récupéré le nom")
            return nom_president


def donner_prenom(nom_president):
    prenom_pre = ""
    if nom_president == "Chirac":
        prenom_pre = "Jacques"
        print("On a donné un prénom")
    if nom_president == "Giscard dEstaing":
        prenom_pre = "Valery"
        print("On a donné un prénom")
    if nom_president == "Hollande":
        prenom_pre = "François"
        print("On a donné un prénom")
    if nom_president == "Mitterrand":
        prenom_pre = "François"
        print("On a donné un prénom")
    if nom_president == "Macron":
        prenom_pre = "Emmanuel"
        print("On a donné un prénom")
    if nom_president == "Sarkozy":
        prenom_pre = "Nicolas"
        print("On a donné un prénom")

    return prenom_pre

def copier_texte(nom_fichier):
    contenu_fichier = ""
    with open(nom_fichier, 'r',encoding='utf8') as fichier:
        contenu_fichier = fichier.read()
    print("On a récupéré le contenu")
    return contenu_fichier

def convertir_en_minuscules(contenu_fichier):
    contenu_minus = contenu_fichier.lower()
    print("On a converti en minuscules")
    return contenu_minus

def transferer_contenu(contenu_minus, nom_fichier):
    nom_desti = nom_fichier
    if not os.path.exists("./ressources/cleaned"):
        os.mkdir("./ressources/cleaned") #On crée un répertoire cleaned
    if not os.path.exists("./ressources/cleaned/nom_desti"):
        with open("./ressources/cleaned/"+nom_desti, 'w',encoding='utf8') as fichier_destination:
            fichier_destination.write(contenu_minus) #On crée un fichier texte en minuscule dans le répertoire cleaned
    fichier_destination.close()
def nettoyer_texte(nom_fichier):
    chemin_fichier = "./ressources/cleaned/" + nom_fichier
    with open(chemin_fichier, 'r', encoding='utf8') as fichier:
        contenu = fichier.read()
    contenu_sans_ponctuation = ''.join(caractere if caractere not in string.punctuation else ' ' for caractere in contenu)
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