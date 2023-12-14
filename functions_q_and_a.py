from functions_Presidents_Speeches import *
from functions_TF_IDF_Matrice import *
def tokeniser_question(quest):
    mots = quest.split()
    liste_mots = list(mots)
    return liste_mots


def rechercher_mot_quest(liste_mots, mots_corpus):
    liste_inter = []
    for mot in liste_mots:
        if mot in mots_corpus :
            liste_inter.append(mot)
    return liste_inter