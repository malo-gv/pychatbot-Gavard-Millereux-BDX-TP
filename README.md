# pychatbot-Gavard-Millereux-BDX-TP
Malo GAVARD
Noé MILLEREUX

BUG NOTABLES:

Il arrive que lors du lancement du programme on est l'erreur suivante :
"PermissionError: [Errno 13] Permission denied"
Pour résoudre ce problème il suffit de relancer le programme plusieurs fois.

Précautions à prendre avant d'utiliser le programme :
Il faut préalablement récupérer les discours de tous les président et les mettres dans un répertoire dans le programme python

Fonctions Principales

Fonction: list_of_files(directory, extension)
Utilisation: Récupère la liste des fichiers dans le répertoire spécifié avec l'extension donnée.

Nom du Président:
Fonctions: donner_nom(nom_fichier), donner_prenom(nom_president)
Utilisation: Obtient le nom du président à partir du nom du fichier et récupère son prénom associé.

Nettoyer le Texte:
Fonction: nettoyer_texte(nom_fichier)
Utilisation: Supprime la ponctuation et normalise le texte pour faciliter l'analyse.

Calcul du TF-IDF:
Fonctions: calculer_tf(nom_fichier), calculer_idf(directory), generer_matrice(directory)
Utilisation: Calcul du score TF-IDF pour les mots dans les discours présidentiels.

Mots les Moins Importants:
Fonction: mots_non_importants(directory)
Utilisation: Identifie les mots ayant un score IDF nul (les moins importants).

Mot le Plus Important:
Fonction: mot_plus_important(directory)
Utilisation: Trouve le mot avec le score TF-IDF le plus élevé dans l'ensemble des discours.

Mots les Plus Répétés par Chirac:
Fonction: mots_plus_repetes_par_chirac(directory)
Utilisation: Identifie les mots les plus fréquemment utilisés dans les discours de Chirac.

Président Parlant de la Nation:
Fonction: president_nation(directory)
Utilisation: Trouve les présidents parlant de la "Nation" et celui qui en parle le plus.

Président Parlant d'Écologie:
Fonction: president_ecologie(directory)
Utilisation: Identifie le premier président à parler du climat et/ou de l'écologie.

Mots Évoqués par Tous les Présidents:
Fonction: mots_evoques(directory)
Utilisation: Trouve les mots communs mentionnés par tous les présidents.

Fonction : copier_texte(nom_fichier)
Utilisation : Copie le contenu du fichier spécifié.

Fonction : convertir_en_minuscules(contenu_fichier)
Utilisation : Convertit le contenu du fichier en minuscules.

Fonction : transferer_contenu(contenu_minus, nom_fichier)
Utilisation : Transfère le contenu en minuscules vers un nouveau fichier dans le répertoire "cleaned".

Fonction : extraire_phrase_contenant_mot2(contenu, mot_max_tfidf)
Utilisation : Extrait la première phrase du contenu contenant le mot avec le score TF-IDF le plus élevé.

Fonction : generer_reponse(question, directory, document_pertinent_name, tfidf_question)
Utilisation : Génère une réponse à partir de la question en utilisant le document pertinent, son nom, et le vecteur TF-IDF de la question.
