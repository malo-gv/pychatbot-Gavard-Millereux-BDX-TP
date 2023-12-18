from functions_Presidents_Speeches import donner_nom, donner_prenom
from functions_TF_IDF_Matrice import *

"""def extraire_phrase_contenant_mot(contenu, mot_max_tfidf):
    # Liste de délimiteurs de phrases
    delimitateurs = ['.', '!', '?']
    phrase = ""
    for i in range(len(contenu)):
        if contenu[i] in delimitateurs :
            for j in range(i+1,len(contenu)):"""



def generer_reponse(question, directory, document_pertinent_name, tfidf_question):
    # Étape 2 : Trouver le mot ayant le score TF-IDF le plus élevé
    mot_max_tfidf_index = tfidf_question.index(max(tfidf_question))
    liste_mots_question = tokeniser_question(question)
    mot_max_tfidf = liste_mots_question[mot_max_tfidf_index]
    print(mot_max_tfidf)
    print("Document pertinent trouvé :", document_pertinent_name)  # Ajout d'une impression

    # Utiliser la fonction donner_nom pour extraire le nom et le prénom du président
    nom_president = donner_nom(document_pertinent_name)
    prenom_president = donner_prenom(nom_president)

    # Étape 4 : Trouver la première occurrence du mot dans le document pertinent
    chemin_document_pertinent = os.path.join(directory, document_pertinent_name)
    with open(chemin_document_pertinent, 'r', encoding='utf8') as fichier:
        contenu_document_pertinent = fichier.read()
    # Utiliser la fonction pour extraire la phrase

    phrase_contenant_mot = extraire_phrase_contenant_mot2(contenu_document_pertinent, mot_max_tfidf)

    # Formater la réponse en incluant le nom du président
    reponse = f"Le président {prenom_president} {nom_president} a dit : {phrase_contenant_mot}"

    return reponse
