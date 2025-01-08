import random


def chiffrage(texte:str, decalage:int) -> str:
    """ chiffre le texte avec le decalage """
    dictionnaire_decalage = {chr(i+65):chr((i+decalage) %58+65) for i in range(58)}
    chaine_fin = ""
    for i in texte:
        if i == " ":
            chaine_fin += " "
        else:
            chaine_fin += dictionnaire_decalage.get(i)
    return chaine_fin



def dechiffrage(texte:str, decalage:int) -> str:
    """ dechiffre le texte avec le decalage """
    dictionnaire_decalage = {chr(i+65):chr((i-decalage) %58+65) for i in range(58)}
    chaine_fin = ""
    for i in texte:
        if i == " ":
            chaine_fin += " "
        else:
            chaine_fin += dictionnaire_decalage.get(i)
    return chaine_fin


def dechiffrage_maj(texte:str, decalage:int) -> str:
    """
    dechiffre le texte avec le decalage
    (!) Uniquement avec le majuscules sans espaces
    """
    dictionnaire_decalage = {chr(i+65):chr((i+decalage) %26+65) for i in range(26)}
    chaine_fin = ""
    for i in texte.upper():
        if dictionnaire_decalage.get(i) != None:
            chaine_fin += str(dictionnaire_decalage.get(i))
    return chaine_fin