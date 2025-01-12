import customtkinter as ctk
import dechiffrage as dech
import chiffre_dechiffre as ch_dech



def ch_update_label(decalage):
    """ récupère les entrées et lance le code associé si il y a un texte """
    ch_str_decalage.configure(text="Decalage de "+str(round(decalage)))
    texte = ch_str_entree.get()
    if texte != '':
        sortie = ch_dech.chiffrage(texte, round(decalage))
        ch_str_sortie.configure(state="normal")
        ch_str_sortie.delete("1.0", ctk.END)
        ch_str_sortie.insert(ctk.END, sortie)
        ch_str_sortie.configure(state="disabled")
        box.update()


def dech_update_label(decalage):
    """ récupère les entrées et lance le code associé si il y a un texte """
    ch_str_decalage.configure(text="Decalage de "+str(round(decalage)))
    texte = ch_str_entree.get()
    if texte != '':
        sortie = ch_dech.dechiffrage(texte, round(decalage))
        ch_str_sortie.configure(state="normal")
        ch_str_sortie.delete("1.0", ctk.END)
        ch_str_sortie.insert(ctk.END, sortie)
        ch_str_sortie.configure(state="disabled")
        box.update()


# variables
taille = 4
# textes
texte_grand = ('Arial', 18, 'bold')
texte_petit = ('Arial', 14)
# couleurs
color_groupes = "#505050"


"""
ch -> chiffrement
dech -> dechiffrement
avdech -> dechiffrement avancé
"""


# parametres de la fenetre
box = ctk.CTk()
box.geometry("400x300")
box.title("Code César")
box.iconbitmap('./icone.ico')


                                  ### ___ parties ___ ###


### ___ chiffrement ___ ###
# boite
ch_box = ctk.CTkFrame(master=box, width=400, height=200, corner_radius=15)
ch_box.pack(pady=10, padx=10, fill="both", expand=True)
ctk.CTkLabel(master=ch_box, text="Chiffrement", font=texte_grand).pack(pady=10)

# entrée utilisateur
ch_str_entree = ctk.CTkEntry(master=ch_box, placeholder_text="Entrez le texte à chiffrer ...")
ch_str_entree.pack(pady=10, fill="x", padx=20)

# barre de decalage
ch_str_decalage = ctk.CTkLabel(master=ch_box, text="decalage de 0", font=texte_petit)
ch_str_decalage.pack(pady=(10,0))
ch_decalage = ctk.CTkSlider(master=ch_box, from_=0, to=26, command=ch_update_label, number_of_steps=26)
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
dech_box.pack(pady=10, padx=10, fill="both", expand=True)
ctk.CTkLabel(master=dech_box, text="Déchiffrement", font=texte_grand).pack(pady=10)

# entrée utilisateur
dech_str_entree = ctk.CTkEntry(master=dech_box, placeholder_text="Entrez le texte à déchiffrer ...")
dech_str_entree.pack(pady=10, fill="x", padx=20)

# barre de decalage
dech_str_decalage = ctk.CTkLabel(master=dech_box, text="decalage de 0", font=texte_petit)
dech_str_decalage.pack(pady=(10,0))
dech_decalage = ctk.CTkSlider(master=dech_box, from_=0, to=26, command=dech_update_label, number_of_steps=26)
dech_decalage.set(0)
dech_decalage.pack(pady=(0, 10))

# sortie
ctk.CTkLabel(master=dech_box, text="Texte déchiffré :", font=texte_petit).pack(pady=(10,0))
dech_str_sortie = ctk.CTkTextbox(master=dech_box, height=100, wrap="word")
dech_str_sortie.pack(pady=(0,10), fill="x", padx=20)
dech_str_sortie.insert("1.0", "")
dech_str_sortie.configure(state="disabled")










# affichage de la fenetre
box.mainloop()