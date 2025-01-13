import random


def code(texte:str, decalage:int) -> str:
    """ chiffre le texte avec le decalage """
    dictionnaire_decalage = cree_dictionnaire_decalage(decalage)
    chaine_fin = ""
    for i in texte:
        chaine_fin += dictionnaire_decalage.get(i)
    return chaine_fin



def decode(texte:str, decalage:int) -> str:
    """ dechiffre le texte avec le decalage """
    dictionnaire_decalage = cree_dictionnaire_decalage(-decalage)
    chaine_fin = ""
    for i in texte:
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





def cree_dictionnaire_decalage(decalage:int) -> dict:
    """ crée un dictionnaire avec un decalage de decalage """
    symboles_dans_dictionnaire = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)] + [" "]
    dictionnaire = {}
    for i in enumerate(symboles_dans_dictionnaire):
        dictionnaire[i[1]] = symboles_dans_dictionnaire[i[0]+decalage if i[0]+decalage < len(symboles_dans_dictionnaire) else i[0] - len(symboles_dans_dictionnaire) + decalage]
    return dictionnaire


print(len(cree_dictionnaire_decalage(4)))