def code(texte:str, decalage:int) -> str:
    """ chiffre le texte avec le decalage """
    return "".join([cree_dictionnaire_decalage(decalage).get(i) for i in texte])



def decode(texte:str, decalage:int) -> str:
    """ dechiffre le texte avec le decalage """
    return "".join([cree_dictionnaire_decalage(-decalage).get(i) for i in texte])


def dechiffrage_maj(texte:str, decalage:int) -> str:
    """
    dechiffre le texte avec le decalage
    (!) Uniquement avec le majuscules sans espaces
    """
    return "".join([{chr(i+65):chr((i+decalage) %26+65) for i in range(26)}.get(i) if i != None else "" for i in texte.upper()])



def cree_dictionnaire_decalage(decalage:int) -> dict:
    """ crée un dictionnaire avec un decalage de decalage """
    symboles_dans_dictionnaire = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)] + [" "]
    return {i[1] : symboles_dans_dictionnaire[i[0]+decalage if i[0]+decalage < len(symboles_dans_dictionnaire) else i[0] - len(symboles_dans_dictionnaire) + decalage] for i in enumerate(symboles_dans_dictionnaire)}