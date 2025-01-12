import customtkinter as ctk
from tkinter import messagebox

# Configuration initiale
ctk.set_appearance_mode("dark")  # Options : "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Options : "blue", "green", "dark-blue"

# Fenêtre principale
app = ctk.CTk()
app.geometry("600x400")
app.title("Widgets personnalisés")

# Fonction pour récupérer et afficher le texte saisi
def afficher_texte():
    texte_saisi = entry.get()
    if texte_saisi.strip():
        messagebox.showinfo("Texte Saisi", f"Vous avez écrit : {texte_saisi}")
    else:
        messagebox.showwarning("Attention", "Le champ de saisie est vide.")

# Fonction pour copier le code affiché dans la zone de texte
def copier_code():
    code = code_zone.get("1.0", "end-1c")  # Récupérer tout le texte
    app.clipboard_clear()
    app.clipboard_append(code)
    app.update()  # Nécessaire pour que le contenu soit effectivement copié
    messagebox.showinfo("Copié", "Le code a été copié dans le presse-papiers.")

# Cadre principal
frame = ctk.CTkFrame(master=app, width=500, height=350, corner_radius=15)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Widgets pour le texte utilisateur
label_texte = ctk.CTkLabel(master=frame, text="Entrez un texte :", font=("Arial", 14))
label_texte.pack(pady=10)

entry = ctk.CTkEntry(master=frame, placeholder_text="Tapez ici votre texte...")
entry.pack(pady=10, fill="x", padx=20)

button_texte = ctk.CTkButton(master=frame, text="Afficher le texte", command=afficher_texte)
button_texte.pack(pady=10)

# Widgets pour afficher et copier du code
label_code = ctk.CTkLabel(master=frame, text="Code à copier :", font=("Arial", 14))
label_code.pack(pady=10)

code_zone = ctk.CTkTextbox(master=frame, height=100, wrap="word")
code_zone.pack(pady=10, fill="x", padx=20)
code_zone.insert("1.0", "def hello_world():\n    print('Hello, world!')")  # Exemple de code
code_zone.configure(state="disabled")  # Rendre la zone non éditable

button_copier = ctk.CTkButton(master=frame, text="Copier le code", command=copier_code)
button_copier.pack(pady=10)

# Boucle principale
app.mainloop()
