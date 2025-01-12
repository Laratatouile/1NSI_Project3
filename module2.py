import customtkinter as ctk

# Configuration initiale
ctk.set_appearance_mode("dark")  # Options : "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Options : "blue", "green", "dark-blue"

# Fenêtre principale
app = ctk.CTk()
app.geometry("500x400")
app.title("Exemple avec CTkFrame")

# Cadre pour regrouper les widgets
frame = ctk.CTkFrame(master=app, width=400, height=200, corner_radius=15)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Widgets dans le cadre
label = ctk.CTkLabel(master=frame, text="Regroupement de Widgets", font=("Arial", 16))
label.pack(pady=10)

entry = ctk.CTkEntry(master=frame, placeholder_text="Entrez du texte ici")
entry.pack(pady=10)

button = ctk.CTkButton(master=frame, text="Valider", command=lambda: print("Texte saisi :", entry.get()))
button.pack(pady=10)

# Un autre cadre imbriqué
nested_frame = ctk.CTkFrame(master=frame, width=300, height=100, corner_radius=10, fg_color="gray30")
nested_frame.pack(pady=10, padx=10, fill="x")

nested_label = ctk.CTkLabel(master=nested_frame, text="Cadre imbriqué")
nested_label.pack(pady=5)

nested_button = ctk.CTkButton(master=nested_frame, text="Cliquez ici", command=lambda: print("Bouton du cadre imbriqué"))
nested_button.pack(pady=5)

# Boucle principale
app.mainloop()
