import tkinter as tk
import chiffre_dechiffre



def recup_entry():
    if len(nom.get()) == 1 and nom.get() != "":
        global j1
        j1 = nom.get()
        box.destroy()
    else :
        texte.config(text="il y a trop de caractères")




def interface():
    box = tk.Tk()
    box.title("code césar")
    box.minsize(250,150)
    ## textes
    tk.Label(box, text="Entrez votre texte :").pack(padx=10, pady=(0, 10))
    tk.Label(box, text="").pack(padx=10, pady=(0, 10))
    ## boite de saisie
    global nom
    nom = tk.Entry(box)
    nom.focus_set()
    nom.pack(pady=10)
    ## boutons
    tk.Button(box, text="Ok", command=recup_entry).pack(padx=10, pady=(0, 10))
    box.mainloop()


interface()


"""
chiffre = chiffrage(message, decale)
print(chiffre)
dechiffre = dechiffrage(chiffre, decale)
print(dechiffre)"""