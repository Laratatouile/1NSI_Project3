import chiffre_dechiffre as ch_dech


def dechiffrage(texte:str) -> tuple:
    """ fonction principale du dechiffrage du texte """
    # le nombre d'apparition des lettres dans un dictionnaire
    dict_apparitions = dictionnaire(texte)
    # la lettre qui revient le plus souvent
    lettre_plus = le_plus(dict_apparitions)
    # le dictionnaire qui contient chaque lettre dans l'alphabet et son rang dans celui-ci
    dictionnaire_lettre_chiffre = {chr(i): i - 64 for i in range(65, 91)}
    # calcul du decalage a appliquer pour retrouver le texte d'origine
    decalage = 5 - dictionnaire_lettre_chiffre[lettre_plus]
    # dechffrage du texte a l'aide du module de chiffrage_dechiffrage
    texte_dechiffre = ch_dech.dechiffrage_maj(texte, decalage)
    return texte_dechiffre, -decalage




def le_plus(dictionnaire:dict) -> str:
    """ calcul de la lettre qui revient le plus souvent """
    lettre_max = ["", 0]
    for i in dictionnaire:
        if dictionnaire[i] > lettre_max[1]:
            lettre_max = [i, dictionnaire[i]]
    return lettre_max[0]


def dictionnaire(texte:str) -> dict:
    """ compte le nombre d'apparition des lettres dans le texte """
    dictionnaire = {}
    for i in texte:
        if i in dictionnaire:
            dictionnaire[i] += 1
        else:
            dictionnaire[i] = 1
    return dictionnaire