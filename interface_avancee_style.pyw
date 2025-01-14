import customtkinter as ctk
import dechiffrage as dech
import chiffre_dechiffre as ch_dech



def ch_update_label(decalage:int) -> None:
    """ récupère les entrées et lance le code associé si il y a un texte """
    ch_str_decalage.configure(text="Decalage de "+str(round(decalage)))
    texte = ch_str_entree.get()
    if texte != '':
        sortie = ch_dech.code(texte, round(decalage))
        ch_str_sortie.configure(state="normal")
        ch_str_sortie.delete("1.0", ctk.END)
        ch_str_sortie.insert(ctk.END, sortie)
        ch_str_sortie.configure(state="disabled")
        box.update()


def dech_update_label(decalage:int) -> None:
    """ récupère les entrées et lance le code associé si il y a un texte """
    dech_str_decalage.configure(text="Decalage de "+str(round(decalage)))
    texte = dech_str_entree.get()
    if texte != '':
        sortie = ch_dech.decode(texte, round(decalage))
        dech_str_sortie.configure(state="normal")
        dech_str_sortie.delete("1.0", ctk.END)
        dech_str_sortie.insert(ctk.END, sortie)
        dech_str_sortie.configure(state="disabled")
        box.update()


def avdech_update_label() -> None:
    """ récupère les entrées et lance le code associé si il y a un texte """
    texte = avdech_str_entree.get()
    if texte != '':
        sortie = dech.dechiffrage(texte.upper())
        avdech_str_sortie.configure(state="normal")
        avdech_str_sortie.delete("1.0", ctk.END)
        avdech_str_sortie.insert(ctk.END, sortie[0])
        avdech_str_sortie.configure(state="disabled")
        avdech_str_dec.configure(text="Décalage : "+str(sortie[1]))
        box.update()


# variables
taille = 4
nombre_caracteres = 63
# textes
texte_grand = ('Arial', 18, 'bold')
texte_petit = ('Arial', 14)
texte_bouton = ('Arial', 14, 'bold')
# couleurs
color_groupes = "#505050"


"""
ch -> chiffrement
dech -> dechiffrement
avdech -> dechiffrement avancé
"""


# parametres de la fenetre
box = ctk.CTk()
box.geometry("900x350")
box.title("Code César")
box.iconbitmap('./icone.ico')
box.minsize(900, 350)

                                  ### ___ parties ___ ###


### ___ chiffrement ___ ###
# boite
ch_box = ctk.CTkFrame(master=box, width=400, height=200, corner_radius=15)
ch_box.pack(pady=10, padx=10, fill="both", expand=True, side="left")
ctk.CTkLabel(master=ch_box, text="Chiffrement", font=texte_grand).pack(pady=10)

# entrée utilisateur
ch_str_entree = ctk.CTkEntry(master=ch_box, placeholder_text="Entrez le texte à chiffrer ...")
ch_str_entree.pack(pady=10, fill="x", padx=20)

# barre de decalage
ch_str_decalage = ctk.CTkLabel(master=ch_box, text="decalage de 0", font=texte_petit)
ch_str_decalage.pack(pady=(10,0))
ch_decalage = ctk.CTkSlider(master=ch_box, from_=0, to=nombre_caracteres, command=ch_update_label, number_of_steps=nombre_caracteres)
ch_decalage.set(0)
ch_decalage.pack(pady=(0, 10))

# sortie
ctk.CTkLabel(master=ch_box, text="Texte chiffré :", font=texte_petit).pack(pady=(10,0))
ch_str_sortie = ctk.CTkTextbox(master=ch_box, height=100, wrap="word")
ch_str_sortie.pack(pady=(0,10), fill="x", padx=20)
ch_str_sortie.insert("1.0", "")
ch_str_sortie.configure(state="disabled")



### ___ dechiffrement ___ ###
# boite
dech_box = ctk.CTkFrame(master=box, width=400, height=200, corner_radius=15)
dech_box.pack(pady=10, padx=10, fill="both", expand=True, side="left")
ctk.CTkLabel(master=dech_box, text="Déchiffrement", font=texte_grand).pack(pady=10)

# entrée utilisateur
dech_str_entree = ctk.CTkEntry(master=dech_box, placeholder_text="Entrez le texte à déchiffrer ...")
dech_str_entree.pack(pady=10, fill="x", padx=20)

# barre de decalage
dech_str_decalage = ctk.CTkLabel(master=dech_box, text="decalage de 0", font=texte_petit)
dech_str_decalage.pack(pady=(10,0))
dech_decalage = ctk.CTkSlider(master=dech_box, from_=0, to=nombre_caracteres, command=dech_update_label, number_of_steps=nombre_caracteres)
dech_decalage.set(0)
dech_decalage.pack(pady=(0, 10))

# sortie
ctk.CTkLabel(master=dech_box, text="Texte déchiffré :", font=texte_petit).pack(pady=(10,0))
dech_str_sortie = ctk.CTkTextbox(master=dech_box, height=100, wrap="word")
dech_str_sortie.pack(pady=(0,10), fill="x", padx=20)
dech_str_sortie.insert("1.0", "")
dech_str_sortie.configure(state="disabled")



### ___ dechiffrement avance ___ ###
# boite
avdech_box = ctk.CTkFrame(master=box, width=400, height=200, corner_radius=15)
avdech_box.pack(pady=10, padx=10, fill="both", expand=True, side="left")
ctk.CTkLabel(master=avdech_box, text="Déchiffrement avancé", font=texte_grand).pack(pady=10)

# entrée utilisateur
avdech_str_entree = ctk.CTkEntry(master=avdech_box, placeholder_text="Entrez le texte à déchiffrer ...")
avdech_str_entree.pack(pady=10, fill="x", padx=20)

# bouton de dechiffrage
ctk.CTkButton(avdech_box, text="Déchiffrer", command=avdech_update_label, fg_color='#555555', hover_color='#444444').pack(pady=(0, 10))

# sortie
avdech_str_dec = ctk.CTkLabel(master=avdech_box, text="Décalage : ", font=texte_petit)
avdech_str_dec.pack(pady=(10,0))

ctk.CTkLabel(master=avdech_box, text="Texte déchiffré :", font=texte_petit).pack()
avdech_str_sortie = ctk.CTkTextbox(master=avdech_box, height=100, wrap="word")
avdech_str_sortie.pack(pady=(0,10), fill="x", padx=20)
avdech_str_sortie.insert("1.0", "")
avdech_str_sortie.configure(state="disabled")





# affichage de la fenetre
box.mainloop()