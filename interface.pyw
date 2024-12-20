import tkinter as tk
import chiffre_dechiffre as ch_dech



def recup_entry_ch():
    texte = txt_ch.get()
    decalage = int(dec_ch.get())
    sortie = ch_dech.chiffrage(texte, decalage)
    data_string_ch.set(sortie)
    

def recup_entry_dech():
    texte = txt_dech.get()
    decalage = int(dec_dech.get())
    sortie = ch_dech.dechiffrage(texte, decalage)
    data_string_dech.set(sortie)





box = tk.Tk()
box.title("code césar")
box.minsize(500,250)



### ___ pannel de chiffrage ___ ###
## pannels
chiffrage_box = tk.LabelFrame(box, text="Chiffrage", padx=20, pady=20)
chiffrage_box.pack(fill="both", side=tk.LEFT, expand="yes")
## boite de saisie
# texte
tk.Label(chiffrage_box, text="Entrez votre texte :").pack(padx=10)
txt_ch = tk.Entry(chiffrage_box)
txt_ch.focus_set()
txt_ch.pack(pady=10)
# decalage
tk.Label(chiffrage_box, text="Decalage des caractères :").pack(padx=10)
dec_ch = tk.Entry(chiffrage_box)
dec_ch.pack(pady=10)
## boutons
tk.Button(chiffrage_box, text="Ok", command=recup_entry_ch).pack(padx=10, pady=(0, 10))
# sortie
tk.Label(chiffrage_box, text="Texte chiffré :").pack(padx=10)
data_string_ch = tk.StringVar()
data_string_ch.set("")
ent = tk.Entry(chiffrage_box, textvariable=data_string_ch, bd=0, state="readonly")
ent.pack()




### ___ pannel de dechiffrage ___ ###
## pannels
dechiffrage_box = tk.LabelFrame(box, text="Dechiffrage", padx=20, pady=20)
dechiffrage_box.pack(fill="both", side=tk.RIGHT, expand="yes")
## boite de saisie
# texte
tk.Label(dechiffrage_box, text="Entrez votre texte :").pack(padx=10)
txt_dech = tk.Entry(dechiffrage_box)
txt_dech.pack(pady=10)
# decalage
tk.Label(dechiffrage_box, text="Decalage des caractères :").pack(padx=10)
dec_dech = tk.Entry(dechiffrage_box)
dec_dech.pack(pady=10)
## boutons
tk.Button(dechiffrage_box, text="Ok", command=recup_entry_dech).pack(padx=10, pady=(0, 10))
# sortie
tk.Label(dechiffrage_box, text="Texte dechiffré :").pack(padx=10)
data_string_dech = tk.StringVar()
data_string_dech.set("")
ent = tk.Entry(dechiffrage_box, textvariable=data_string_dech, bd=0, state="readonly")
ent.pack()


box.mainloop()



"""
chiffre = chiffrage(message, decale)
print(chiffre)
dechiffre = dechiffrage(chiffre, decale)
print(dechiffre)"""