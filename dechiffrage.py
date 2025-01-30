def  dechiffrage(texte:str) -> str:
    """fonction principale du dechiffrage du texte"""

    dictionnaire_apparition = {}
    for lettre in texte:
        if lettre in dictionnaire_apparition:
            dictionnaire_apparition[lettre] += 1
        else:
            dictionnaire_apparition[lettre] = 1
    lettre_max = ""
    maximum = 0
    for i,j in dictionnaire_apparition.items():
        if j > maximum:
            maximum = j
            lettre_max = i

    print(lettre_max)

    alphabet_dict = {chr(i): i - 64 for i in range(65, 91)}
    decalage = alphabet_dict[lettre_max] - 5

    d = {chr(i+65):chr((i-decalage) %26+65) for i in range(26)}
    sortie = ""

    for lettre in texte:
        sortie += d[lettre]
    return sortie, decalage

