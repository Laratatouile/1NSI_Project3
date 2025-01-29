# 1NSI_Project3
## informations
Travail de NSI (mini project 3)
ce mini project a pour but de créer une interface de chiffrement.

## demarrage
Pour demarrer le programme:
- demarrer "interface_simple" pour une interface simple
- demarrer "interface_style" pour une interface au style plus moderne


## carnet de bord
### 20 décembre maxime:
- découverte du project 3
- création du GitHub
- création du programme qui permet de générer les codes césars
- création de l'extention d'interface graphique avec Tkinter
- création du logo de l'interface


### Janvier 2025 maxime:
- création d'une autre interface avec custom Tkinter
- résolution de bugs sur le systeme de chiffrement (dictionnaire de chiffrement)
- mise en place de création de listes et de dictionnaire par compréhention
- mise en place du bouton copier



## comment fonctionne le code:
### les fichiers interfaces_...pyw:
Ces fichies sont destinées à être executés par l'utilisateur

(!) les interfaces avancee et minimisee requierent l'installation de customtkinter pour fonctionner
Vous pouvez l'installer avec la commande
`pip install customtkinter`
dans un terminal

ces fichiers contienent uniquement les fichiers nécéssaires aux interfaces


### le fichier chiffrage_dechiffrage:
Ce fichier contient plusieurs fonctions:
- celle qui genere un dictionnaire a partir d'un decalage
- celle qui utilise un dictionnaire de decalage pour transformer un texte en texte chiffré
- celle qui fait l'inverse et utilise un dictionnaire de decalage pour dechiffrer un texte
- et celle un peu spéciale qui permet de dechiffrer un texte fait d'uniquement des majuscules

### le fichier dechiffrage:
ce fichier est spécialisé dans le dechiffrage des longs textes et a pour avantage de ne pas demander de clef de dechiffrage à l'utilisateur
Ce fichier utilise plusieurs fonctions pour fonctionner:
- une fonction qui permet de mettre chaque lettre avec son nombre d'apparttion dans un dectionnaire
- une qui cherche la lettre la plus présente dans le dictionnaire et la récupère

Le script calcule ensuite le decalage avec un dictionnaire qui possède chaque lettre et sa position dans l'alphabet

Il envoie ensuite le texte chiffré au fichier de dechiffrage avec la clef qu'il à trouvé
