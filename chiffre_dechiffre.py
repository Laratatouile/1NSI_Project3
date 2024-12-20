import random


def chiffrage(texte:str, decalage:int) -> str:
    dictionnaire_decalage = {chr(i+65):chr((i+decalage) %26+65) for i in range(26)}
    chaine_fin = ""
    for i in texte:
        if i == " ":
            chaine_fin += " "
        else:
            chaine_fin += dictionnaire_decalage.get(i.upper())
    return chaine_fin.lower()



def dechiffrage(texte:str, decalage:int) -> str:
    dictionnaire_decalage = {chr(i+65):chr((i-decalage) %26+65) for i in range(26)}
    chaine_fin = ""
    for i in texte:
        if i == " ":
            chaine_fin += " "
        else:
            chaine_fin += dictionnaire_decalage.get(i.upper())
    return chaine_fin.lower()

