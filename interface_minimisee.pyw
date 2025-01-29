import customtkinter as ctk
import dechiffrage as av_dech
import chiffre_dechiffre as ch_dech


# Création de la fenêtre principale
box = ctk.CTk()
box.title("Code César")
box.iconbitmap('./icone.ico')
box.geometry("500x430")
box.minsize(500, 430)

ancien_int = ""
mode_selection = ctk.StringVar(value="Chiffrement")

# Création du cadre pour les boutons radio
radio_frame = ctk.CTkFrame(box)
radio_frame.pack(fill="x", pady=10, padx=10)


# variables
ch_sortie = ""
dech_sortie = ""
avdech_sortie = ""

# Listes des interfaces
ch, dech, avdech = [], [], []


# affichage en chiffrement
def ch_affichage(decalage:int) -> None:
    """ prend en parametre les widgets et les affiches sur la barre du slider et réalise le decalage """
    texte = ch[2].get()
    ch[3].configure(text="Decalage de "+str(round(decalage)))
    if texte != '':
        global ch_sortie
        ch_sortie = ch_dech.code(texte, round(decalage))
        ch[6].configure(state="normal")
        ch[6].delete("1.0", ctk.END)
        ch[6].insert(ctk.END, ch_sortie)
        ch[6].configure(state="disabled")
        box.update()
    return None


# affichage en dechiffrement
def dech_affichage(decalage:int) -> None:
    """ prend en parametre les widgets et les affiches sur la barre du slider et réalise le decalage """
    texte = dech[2].get()
    dech[3].configure(text="Decalage de "+str(round(decalage)))
    if texte != '':
        global dech_sortie
        dech_sortie = ch_dech.decode(texte, round(decalage))
        dech[6].configure(state="normal")
        dech[6].delete("1.0", ctk.END)
        dech[6].insert(ctk.END, dech_sortie)
        dech[6].configure(state="disabled")
        box.update()
    return None


# affichage en dechiffrement avance
def avdech_affichage() -> None:
    """ récupère les entrées et lance le code associé si il y a un texte """
    texte = avdech[2].get()
    if texte != '':
        global avdech_sortie
        avdech_sortie = av_dech.dechiffrage(texte.upper())
        avdech[6].configure(state="normal")
        avdech[6].delete("1.0", ctk.END)
        avdech[6].insert(ctk.END, avdech_sortie[0])
        avdech[6].configure(state="disabled")
        avdech[4].configure(text="Décalage : "+str(avdech_sortie[1]))
        box.update()
    return None




# changements de l'interface
def switch_interface() -> None:
    """ change l'interface en fonction de l'interface précédente """
    global ancien_int
    selected = mode_selection.get()
    if selected == "Chiffrement":
        selected = "ch"
    elif selected == "Déchiffrement":
        selected = "dech"
    else:
        selected = "avdech"

    # nouvelle interface: chiffrement
    if selected == "ch" and ancien_int != "ch":
        for widget in (dech if ancien_int == "dech" else avdech):
            widget.pack_forget()
        ch[0].pack(pady=10, padx=10, fill="both", expand=True, side="left")
        ch[1].pack(pady=10)
        ch[2].pack(pady=10, fill="x", padx=20)
        ch[3].pack(pady=(10,0))
        ch[4].pack(pady=(0, 10))
        ch[5].pack(pady=(10,0))
        ch[6].pack(pady=(0,10), fill="x", padx=20)
        ch[7].pack(pady=(0, 10))
        box.geometry("500x430")
        ancien_int = "ch"
    # nouvelle interface: dechiffrement
    elif selected == "dech" and ancien_int != "dech":
        for widget in (ch if ancien_int == "ch" else avdech):
            widget.pack_forget()
        dech[0].pack(pady=10, padx=10, fill="both", expand=True, side="left")
        dech[1].pack(pady=10)
        dech[2].pack(pady=10, fill="x", padx=20)
        dech[3].pack(pady=(10,0))
        dech[4].pack(pady=(0, 10))
        dech[5].pack(pady=(10,0))
        dech[6].pack(pady=(0,10), fill="x", padx=20)
        dech[7].pack(pady=(0, 10))
        box.geometry("500x430")
        ancien_int = "dech"
    # nouvelle interface: dechiffrement avance
    elif ancien_int != "avdech":
        for widget in (ch if ancien_int == "ch" else dech):
            widget.pack_forget()
        avdech[0].pack(pady=10, padx=10, fill="both", expand=True, side="left")
        avdech[1].pack(pady=10)
        avdech[2].pack(pady=10, fill="x", padx=20)
        avdech[3].pack(pady=(0, 10))
        avdech[4].pack(pady=(10,0))
        avdech[5].pack(pady=(0, 10))
        avdech[6].pack(pady=(0,10), fill="x", padx=20)
        avdech[7].pack(pady=(0, 10))
        box.geometry("500x450")
        ancien_int = "avdech"
    return None


# copie le "code" dans le presse papier
def copy_code(code) -> None:
    """ copie le code dans le presse papier """
    box.clipboard_clear()
    box.clipboard_append(code)
    return None




# Création de l'interface de chiffrement
ch.append(ctk.CTkFrame(box))
ch.append(ctk.CTkLabel(ch[0], text="Chiffrement", font=("Arial", 18, "bold")))
ch.append(ctk.CTkEntry(ch[0], placeholder_text="Entrez le texte à chiffrer ..."))
ch.append(ctk.CTkLabel(ch[0], text="Décalage de 0", font=("Arial", 14)))
ch.append(ctk.CTkSlider(ch[0], from_=0, to=63, number_of_steps=63, command=ch_affichage))
ch[4].set(0)
ch.append(ctk.CTkLabel(ch[0], text="Texte chiffré :", font=("Arial", 14)))
ch.append(ctk.CTkTextbox(ch[0], height=100, wrap="word"))
ch[6].configure(state="disabled")
ch.append(ctk.CTkButton(ch[0], text="Copier", fg_color='#555555', hover_color='#444444', command=lambda: copy_code(ch_sortie)))

# Création de l'interface de déchiffrement*
dech.append(ctk.CTkFrame(box))
dech.append(ctk.CTkLabel(dech[0], text="Déchiffrement", font=("Arial", 18, "bold")))
dech.append(ctk.CTkEntry(dech[0], placeholder_text="Entrez le texte à déchiffrer ..."))
dech.append(ctk.CTkLabel(dech[0], text="Décalage de 0", font=("Arial", 14)))
dech.append(ctk.CTkSlider(dech[0], from_=0, to=63, number_of_steps=63, command=dech_affichage))
dech[4].set(0)
dech.append(ctk.CTkLabel(dech[0], text="Texte déchiffré :", font=("Arial", 14)))
dech.append(ctk.CTkTextbox(dech[0], height=100, wrap="word"))
dech[6].configure(state="disabled")
dech.append(ctk.CTkButton(dech[0], text="Copier", fg_color='#555555', hover_color='#444444', command=lambda: copy_code(dech_sortie)))

# Création de l'interface de déchiffrement avancé
frame = ctk.CTkFrame(box)
avdech.append(frame)
avdech.append(ctk.CTkLabel(frame, text="Déchiffrement Avancé", font=("Arial", 18, "bold")))
avdech.append(ctk.CTkEntry(frame, placeholder_text="Entrez le texte à déchiffrer ..."))
avdech.append(ctk.CTkButton(frame, text="Déchiffrer", fg_color='#555555', hover_color='#444444', command=avdech_affichage))
avdech.append(ctk.CTkLabel(frame, text="Décalage :", font=("Arial", 14)))
avdech.append(ctk.CTkLabel(frame, text="Texte déchiffré :", font=("Arial", 14)))
avdech.append(ctk.CTkTextbox(frame, height=100, wrap="word"))
avdech[6].configure(state="disabled")
avdech.append(ctk.CTkButton(frame, text="Copier", fg_color='#555555', hover_color='#444444', command=lambda: copy_code(avdech_sortie)))

# Création des boutons radio
for mode in ["Chiffrement", "Déchiffrement", "Déchiffrement avancé"]:
    ctk.CTkRadioButton(radio_frame, text=mode, variable=mode_selection, value=mode, command=switch_interface).pack(side="left", padx=(10, 10), pady=10)

# Affichage de l'interface par défaut
switch_interface()

box.mainloop()
