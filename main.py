from functions import *

directory = 'ressources/speeches-20231110/'
files_names = (list_of_files(directory, "txt"))
print(list(files_names))  # On affiche la liste des noms de fichiers

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

print("Menu :")
print("1. Calculer le TF pour le discours d'un président spécifique")
print("2. Calculer le IDF pour l'ensemble du corpus")
print("3. Générer la matrice TF-IDF")
print("4. Trouver les mots les plus répétés par Chirac")
print("5. Identifier le président mentionnant 'nation'")
print("6. Identifier le premier président abordant le climat/l'écologie")
print("7. Trouver les mots communs mentionnés par tous les présidents")
print("8. Quitter")

choix = input("Entrez votre choix (1-8) : ")

if choix == '1':
    # Calculer le TF pour le discours d'un président spécifique
    nom_president = input("Entrez le nom du président : ")
    nom_fichier = trouver_fichier_discours(repertoire_discours, nom_president)
    if nom_fichier:
        resultat_tf = calculer_tf(nom_fichier)
        print("TF pour", nom_president, ":", resultat_tf)
    else:
        print("Fichier de discours non trouvé pour", nom_president)

elif choix == '2':
    # Calculer le IDF pour l'ensemble du corpus
    resultat_idf = calculer_idf(repertoire_nettoye)
    print("IDF :", resultat_idf)

elif choix == '3':
    # Générer la matrice TF-IDF
    matrice_tfidf = generer_matrice(repertoire_nettoye)
    print("Matrice TF-IDF :", matrice_tfidf)

elif choix == '4':
    # Trouver les mots les plus répétés par Chirac
    mots_plus_repetes = mots_plus_repetes_par_chirac(repertoire_nettoye)
    print("Mots les plus répétés par Chirac :", mots_plus_repetes)

elif choix == '5':
    # Identifier le président mentionnant 'nation'
    president_nation(repertoire_nettoye)

elif choix == '6':
    # Identifier le premier président abordant le climat/l'écologie
    president_ecologie(repertoire_nettoye)

elif choix == '7':
    # Trouver les mots communs mentionnés par tous les présidents
    mots_evoques(repertoire_nettoye)

elif choix == '8':
    print("Fin du programme. Au revoir !")
    break


















"""
calculer_tf(nom_fichier)
directory = 'ressources/cleaned/'
calculer_idf(directory)

matrice = generer_matrice(directory)

matrice = calculer_transposee(matrice)

mots_non_importants(directory)

"""print(mot_plus_important(directory))"""  # ERREURS VOIR FUNCTIONS

mots_plus_repetes_par_chirac(directory)

president_nation(directory)

president_ecologie(directory)

mots_evoques(directory)
"""