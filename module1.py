import customtkinter as ctk

# Configuration initiale
ctk.set_appearance_mode("dark")  # Options : "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Options : "blue", "green", "dark-blue"

# Fenêtre principale
app = ctk.CTk()
app.geometry("400x300")
app.title("Exemple de CTkSlider")

# Fonction pour afficher la valeur du slider
def update_label(value):
    slider_value_label.configure(text=f"Valeur : {round(float(value), 2)}")

# Curseur (slider)
slider = ctk.CTkSlider(master=app, from_=0, to=100, command=update_label)
slider.pack(pady=20)

# Étiquette pour afficher la valeur du slider
slider_value_label = ctk.CTkLabel(app, text="Valeur : 0")
slider_value_label.pack(pady=10)

# Curseur secondaire avec valeur initiale
slider_secondary = ctk.CTkSlider(master=app, from_=0, to=100, number_of_steps=10)
slider_secondary.set(50)  # Valeur initiale
slider_secondary.pack(pady=20)

# Boucle principale
app.mainloop()
