from functions import *


directory = 'ressources/speeches-20231110/'
files_names = (list_of_files(directory, "txt"))
print(list(files_names)) #On affiche la liste des noms de fichiers


for elt in list(files_names):
    nom_fichier = elt

    Nom = donner_nom(nom_fichier ) #On prend le nom du Président du 5e fichier
    donner_prenom(Nom) #On récupère son prénom en fonction de son nom

    nom_fichier = 'ressources/speeches-20231110/' + nom_fichier
    contenu_fichier = copier_texte(nom_fichier) #On récupère le contenu des fichiers

    contenu_minus = convertir_en_minuscules(contenu_fichier)

    nom_fichier = elt
    transferer_contenu(contenu_minus, nom_fichier)

    nettoyer_texte(nom_fichier)


calculer_tf(nom_fichier)
directory = 'ressources/cleaned/'
calculer_idf(directory)

matrice = generer_matrice(directory)

matrice = calculer_transposee(matrice)

print(mots_non_importants(matrice))