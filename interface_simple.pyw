import tkinter as tk
import chiffre_dechiffre as ch_dech
import dechiffrage as dech



### ___ variables ___ ###
# styles de texte
texte_grand = ("Arial", 18, "bold")
texte_petit = ("Arial", 10)
# couleurs
# -> couleur_arriere_plan : '#535353'
# largeur des colones
largeur = 4


# recuerer l'entrée pour le chiffrage
def recup_entry_ch() -> None:
    """ récupère les entrées et lance le code associé si il y a un texte """
    texte = txt_ch.get()
    if texte != '':
        decalage = int(dec_ch.get())
        sortie = ch_dech.code(texte, decalage)
        data_string_ch.delete("1.0", tk.END)
        data_string_ch.insert(tk.END, sortie)


# recuperer l'entrée pour le dechiffrage
def recup_entry_dech() -> None:
    """ récupère les entrées et lance le code associé si il y a un texte """
    texte = txt_dech.get()
    if texte != '':
        decalage = int(dec_dech.get())
        sortie = ch_dech.decode(texte, decalage)
        data_string_dech.delete("1.0", tk.END)
        data_string_dech.insert(tk.END, sortie)


# recuperer l'entrée pour le dechiffrage avancé
def recup_entry_dech_2() -> None:
    """ récupère les entrées et lance le code associé si il y a un texte """
    texte = txt_dech_2.get().upper()
    if texte != '':
        sortie, decalage = dech.dechiffrage(texte)
        data_string_dech_2.delete("1.0", tk.END)
        data_string_dech_2.insert(tk.END, sortie)
        data_string_dech_2_decalage.delete("1.0", tk.END)
        data_string_dech_2_decalage.insert(tk.END, decalage)



# parametres de la fentre tkinter
box = tk.Tk()
box.title("code césar")
box.minsize(largeur*300,260)
box.iconbitmap('./icone.ico')



### ___ pannel de chiffrage ___ ###
## pannels
chiffrage_box = tk.LabelFrame(box, text="Chiffrage", font=texte_grand, padx=20, pady=20, bg='#535353')
chiffrage_box.pack(side=tk.LEFT, fill=tk.BOTH, expand="yes")
## boite de saisie
# texte
tk.Label(chiffrage_box, text="Entrez votre texte :", bg='#535353', font=texte_petit).pack(padx=10)
txt_ch = tk.Entry(chiffrage_box, width=int(round(largeur*12.5)), bg='#383838', font=texte_petit)
txt_ch.focus_set()
txt_ch.pack(pady=10)
# decalage
tk.Label(chiffrage_box, text="Décalage des caractères :", bg='#535353').pack(padx=10)
dec_ch = tk.Scale(chiffrage_box, orient=tk.HORIZONTAL, from_=0, to=26, length=largeur*85)
dec_ch.pack()
# boutons
tk.Button(chiffrage_box, text="Chiffrer", command=recup_entry_ch,  bg="#999999", fg="white", activebackground="#808080", activeforeground="white", relief="flat", font=texte_petit).pack(padx=10, pady=(30,10))
# sortie
tk.Label(chiffrage_box, text="Texte chiffré :", bg='#535353', font=texte_petit).pack(padx=10, pady=10)
data_string_ch = tk.Text(chiffrage_box, state=tk.NORMAL, height=15, width=int(round(largeur*12.5)), bg='#383838', font=texte_petit)
data_string_ch.pack()




### ___ pannel de dechiffrage ___ ###
## pannels
dechiffrage_box = tk.LabelFrame(box, text="Déchiffrage", font=texte_grand, padx=20, pady=20, bg='#535353')
dechiffrage_box.pack(side=tk.LEFT, fill=tk.BOTH, expand="yes")
## boite de saisie
# texte
tk.Label(dechiffrage_box, text="Entrez votre texte :", bg='#535353', font=texte_petit).pack(padx=10)
txt_dech = tk.Entry(dechiffrage_box, width=int(round(largeur*12.5)), bg='#383838', font=texte_petit)
txt_dech.pack(pady=10)
# decalage
tk.Label(dechiffrage_box, text="Décalage des caractères :", bg='#535353', font=texte_petit).pack(padx=10)
dec_dech = tk.Scale(dechiffrage_box, orient=tk.HORIZONTAL, from_=0, to=26, length=largeur*85)
dec_dech.pack()
## boutons
tk.Button(dechiffrage_box, text="Déchiffrer", command=recup_entry_dech, bg="#999999", fg="white", activebackground="#808080", activeforeground="white", relief="flat", font=texte_petit).pack(padx=10, pady=(30, 10))
# sortie
tk.Label(dechiffrage_box, text="Texte déchiffré :", bg='#535353', font=texte_petit).pack(padx=10, pady=10)
data_string_dech = tk.Text(dechiffrage_box, state=tk.NORMAL, height=15, width=int(round(largeur*12.5)), bg='#383838', font=texte_petit)
data_string_dech.pack()



### ___ pannel de dechiffrage avance ___ ###
## pannels
dechiffrage_box_2 = tk.LabelFrame(box, text="Déchiffrage avancé", font=texte_grand, padx=20, pady=20, bg='#535353')
dechiffrage_box_2.pack(side=tk.LEFT, fill=tk.BOTH, expand="yes")
## boite de saisie
# texte
tk.Label(dechiffrage_box_2, text="Entrez votre texte :", bg='#535353', font=texte_petit).pack(padx=10)
txt_dech_2 = tk.Entry(dechiffrage_box_2, width=int(round(largeur*12.5)), bg='#383838', font=texte_petit)
txt_dech_2.pack(pady=10)
## boutons
tk.Button(dechiffrage_box_2, text="Déchiffrer", command=recup_entry_dech_2, bg="#999999", fg="white", activebackground="#808080", activeforeground="white", relief="flat", font=texte_petit).pack(padx=10, pady=(30, 10))
# sortie
tk.Label(dechiffrage_box_2, text="Decalage du texte :", bg='#535353', font=texte_petit).pack(padx=10, pady=10)
data_string_dech_2_decalage = tk.Text(dechiffrage_box_2, state=tk.NORMAL, height=1, width=int(round(largeur*12.5)), bg='#383838', font=texte_petit)
data_string_dech_2_decalage.pack()
tk.Label(dechiffrage_box_2, text="Texte déchiffré :", bg='#535353', font=texte_petit).pack(padx=10, pady=10)
data_string_dech_2 = tk.Text(dechiffrage_box_2, state=tk.NORMAL, height=15, width=int(round(largeur*12.5)), bg='#383838', font=texte_petit)
data_string_dech_2.pack()


box.mainloop()