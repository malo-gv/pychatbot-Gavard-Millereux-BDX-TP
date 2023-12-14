import string


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
    liste_mots = list(mots)
    return liste_mots

def rechercher_mot_quest(liste_mots, mots_corpus):
    liste_inter = []
    for mot in liste_mots:
        if mot in mots_corpus :
            liste_inter.append(mot)
    return liste_inter

