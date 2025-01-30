import chiffre_dechiffre as ch_dech


def dechiffrage(texte:str) -> tuple:
    """ fonction principale du dechiffrage du texte """
    # le nombre d'apparition des lettres dans un dictionnaire
    dict_apparitions = dictionnaire(texte)
    # la lettre qui revient le plus souvent
    lettre_plus = le_plus(dict_apparitions)
    # calcul du decalage a appliquer pour retrouver le texte d'origine à partir d'un dictionnaire
    # qui contient chaque lettre dans l'alphabet avec son rang
    decalage = 5 - {chr(i): i - 64 for i in range(65, 91)}[lettre_plus]
    # dechffrage du texte a l'aide du module de chiffrage_dechiffrage
    texte_dechiffre = ch_dech.dechiffrage_maj(texte, decalage)
    return texte_dechiffre, -decalage




def le_plus(dictionnaire:dict) -> str:
    """ calcul de la lettre qui revient le plus souvent """
    return max(dictionnaire, key=dictionnaire.get)


def dictionnaire(texte:str) -> dict:
    """ compte le nombre d'apparition des lettres dans le texte """
    return {char: texte.count(char) for char in texte}