# Import des fonctions autres

import os
import math


def list_of_files(directory, extension):  # Ouverture des fichiers
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def donner_nom2(nom_fichier):  # Récupération du nom du président
    nom_president = ""
    for i in range(11,len(nom_fichier)):
        nom_president = nom_president + nom_fichier[i]
        if (nom_fichier[i+1] == ".") or (nom_fichier[i+1] >= '0' and nom_fichier[i+1] <= '9'):
            # On arrête la récupération avant le "." ou un chiffre
            print("TEST")
            return nom_president


def donner_prenom(nom_president):
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
