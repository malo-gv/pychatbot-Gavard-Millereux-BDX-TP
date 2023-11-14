# Import des fonctions autres

import os
import math


def list_of_files(directory, extension):  # Ouverture des fichiers
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def name_of_president(nom_fichier):  # Récupération du nom du président
    nom_president = ""
    for i in range(len(nom_fichier)):
        if nom_fichier[i] == "_":  # On démarre la récupération uniquement après le "_"
            for j in range(i, len(nom_fichier)):
                nom_president = nom_president + nom_fichier[j]
        if nom_fichier[i] == "." or type(nom_fichier[i]) != str:
        # On arrête la récupération avant le "." ou un chiffre
            return nom_president

def first_name(nom_president):
    if nom_president == "Chirac":
        prenom_pre = "Jacques"
    if nom_president == "Giscard dEstaing":
        prenom_pre = "Valery"
    if nom_president == "Hollande" or nom_president == "Mitterand":
        prenom_pre = "François"
    if nom_president == "Macron":
        prenom_pre = "Emmanuel"
    if nom_president == "Sarkozy":
        prenom_pre = "Nicolas"
    nom_complet = prenom_pre + " " + nom_president
    return prenom_pre