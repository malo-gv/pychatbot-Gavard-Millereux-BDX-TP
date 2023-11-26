from functions import *

directory = 'ressources/speeches-20231110/'
files_names = (list_of_files(directory, "txt"))
print("Liste des fichiers :",list(files_names))  # On affiche la liste des noms de fichiers

for elt in list(files_names):
    nom_fichier = elt

    Nom = donner_nom(nom_fichier)  # On prend le nom du Président du 5e fichier
    donner_prenom(Nom)  # On récupère son prénom en fonction de son nom

    nom_fichier = 'ressources/speeches-20231110/' + nom_fichier
    contenu_fichier = copier_texte(nom_fichier)  # On récupère le contenu des fichiers

    contenu_minus = convertir_en_minuscules(contenu_fichier)

    nom_fichier = elt
    transferer_contenu(contenu_minus, nom_fichier)

    nettoyer_texte(nom_fichier)

calculer_tf(nom_fichier)
directory = 'ressources/cleaned/'
calculer_idf(directory)

matrice = generer_matrice(directory)

matrice = calculer_transposee(matrice)

print("Menu :")
print("1. Afficher la liste des mots les moins importants dans le corpus de documents.")
print("2. Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé.")
print("3. Trouver le mot le plus répété par Chirac.")
print("4. Identifier le président parlant de la ""Nation"" et celui en parlant le plus.")
print("5. Indiquer le premier président à parler du climat et/ou de l’écologie.")
print("6. Trouver les mots communs mentionnés par tous les présidents.")
print("7. Annuler.")
print()
print("Si vous obtenez le message ""PermissionError: [Errno 13] Permission denied"" veuillez relancer le programme.")

choix = 0
while choix <= 0 or choix > 7:
    choix = int(input("Entrez votre choix (1-7) : "))
    if choix == 1:
        print("Les mots les moins importants sont : ", mots_non_importants(directory))
        break
    if choix == 2:
        print("Le mot le plus important est : ", mot_plus_important(directory))
        break
    if choix == 3:
        print("Le mot le plus répété par J.Chirac est : ", mots_plus_repetes_par_chirac(directory))
        break
    if choix == 4:
        president_nation(directory)
        break
    if choix == 5:
        print("Le premier président à parler de l'écologie est : ", president_ecologie(directory))
        break
    if choix == 6:
        print("Les mots évoquées par tous les présidents sont : ",mots_evoques(directory))
        break
    if choix == 7:
        print("Fin du programme. Au revoir !")
        break

    else :
        print("! ERREUR !")
        print("Veuillez entrer un chiffre compris entre 1 et 7 SVP !")