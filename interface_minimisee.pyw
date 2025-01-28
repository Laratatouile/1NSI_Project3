import customtkinter as ctk

# Création de la fenêtre principale
box = ctk.CTk()
box.title("Code César")
box.iconbitmap('./icone.ico')
box.geometry("300x400")
box.minsize(300, 400)

ancien_int = ""
mode_selection = ctk.StringVar(value="Chiffrement")

# Création du cadre pour les boutons radio
radio_frame = ctk.CTkFrame(box)
radio_frame.pack(fill="x", pady=10)

# Listes des interfaces
ch, dech, avdech = [], [], []

def affichage(slider, textbox):
    valeur = slider.get()
    texte = textbox.get("1.0", "end").strip()
    print(f"Valeur du slider: {valeur}, Texte: {texte}")

def switch_interface():
    global ancien_int
    selected = mode_selection.get()
    if selected == "Chiffrement":
        selected = "ch"
    elif selected == "Déchiffrement":
        selected = "dech"
    else:
        selected = "avdech"
    print(ancien_int, selected)

    if selected == "ch" and ancien_int != "ch":
        for widget in (dech if ancien_int == "dech" else avdech):
            widget.pack_forget()
        for widget in ch:
            widget.pack()
        ancien_int = "ch"
    elif selected == "dech" and ancien_int != "dech":
        for widget in (ch if ancien_int == "ch" else avdech):
            widget.pack_forget()
        for widget in dech:
            widget.pack()
        ancien_int = "dech"
    elif ancien_int != "avdech":
        for widget in (ch if ancien_int == "ch" else dech):
            widget.pack_forget()
        for widget in avdech:
            widget.pack()
        ancien_int = "avdech"

# Création de l'interface de chiffrement
ch.append(ctk.CTkFrame(box))
ch.append(ctk.CTkLabel(ch[0], text="Chiffrement", font=("Arial", 18, "bold")))
ch.append(ctk.CTkEntry(ch[0], placeholder_text="Entrez le texte à chiffrer ..."))
ch.append(ctk.CTkLabel(ch[0], text="Décalage de 0", font=("Arial", 14)))
slider = ctk.CTkSlider(ch[0], from_=0, to=63, number_of_steps=63)
slider.set(0)
ch.append(slider)
ch.append(ctk.CTkLabel(ch[0], text="Texte chiffré :", font=("Arial", 14)))
textbox = ctk.CTkTextbox(ch[0], height=100, wrap="word")
ch.append(textbox)
ch.append(ctk.CTkButton(ch[0], text="Copier", fg_color='#555555', hover_color='#444444', command=lambda: affichage(slider, textbox)))

# Création de l'interface de déchiffrement*
dech.append(ctk.CTkFrame(box))
dech.append(ctk.CTkLabel(dech[0], text="Déchiffrement", font=("Arial", 18, "bold")))
dech.append(ctk.CTkEntry(dech[0], placeholder_text="Entrez le texte à déchiffrer ..."))
dech.append(ctk.CTkLabel(dech[0], text="Décalage de 0", font=("Arial", 14)))
slider = ctk.CTkSlider(dech[0], from_=0, to=63, number_of_steps=63)
slider.set(0)
dech.append(slider)
dech.append(ctk.CTkLabel(dech[0], text="Texte déchiffré :", font=("Arial", 14)))
textbox = ctk.CTkTextbox(dech[0], height=100, wrap="word")
dech.append(textbox)
dech.append(ctk.CTkButton(dech[0], text="Copier", fg_color='#555555', hover_color='#444444', command=lambda: affichage(slider, textbox)))

# Création de l'interface de déchiffrement avancé
frame = ctk.CTkFrame(box)
avdech.append(frame)
avdech.append(ctk.CTkLabel(frame, text="Déchiffrement Avancé", font=("Arial", 18, "bold")))
avdech.append(ctk.CTkEntry(frame, placeholder_text="Entrez le texte à déchiffrer ..."))
avdech.append(ctk.CTkButton(frame, text="Déchiffrer", fg_color='#555555', hover_color='#444444'))
avdech.append(ctk.CTkLabel(frame, text="Décalage :", font=("Arial", 14)))
avdech.append(ctk.CTkLabel(frame, text="Texte déchiffré :", font=("Arial", 14)))
textbox = ctk.CTkTextbox(frame, height=100, wrap="word")
avdech.append(textbox)
avdech.append(ctk.CTkButton(frame, text="Copier", fg_color='#555555', hover_color='#444444'))

# Création des boutons radio
for mode in ["Chiffrement", "Déchiffrement", "Déchiffrement avancé"]:
    ctk.CTkRadioButton(radio_frame, text=mode, variable=mode_selection, value=mode, command=switch_interface).pack(side="left", padx=5)

# Affichage de l'interface par défaut
switch_interface()

box.mainloop()
