# Créer votre propre interface à l'aide de Tkinter, pour afficher une interface d'inscription donc  Pseudo, mdp, email.
# Et lorsqu'on valide l'inssription ca m'affiche sur le terminal les données 

import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("700x300")
fenetre.title("Exo2 - Login")



etiquette = tk.Label(fenetre, text="Inscrivez vous !")
etiquette.pack()

EmailEtiquette= tk.Label(fenetre, text="Adresse e-mail :")
EmailChamp = tk.Entry(fenetre , width=30)
EmailEtiquette.pack()
EmailChamp.pack()


PseudoEtiquette= tk.Label(fenetre, text="Pseudo :")
PseudoChamp = tk.Entry(fenetre, width=30)
PseudoEtiquette.pack()
PseudoChamp.pack()

MdPEtiquette= tk.Label(fenetre, text="Mot de passe :")
MdPChamp = tk.Entry(fenetre, width=30)
MdPEtiquette.pack()
MdPChamp.pack()

def Inscription() :
    print("Adresse e-mail : " + EmailChamp.get())
    print("Pseudo : " + PseudoChamp.get())
    print("Mot de passe : " + MdPChamp.get())

Submit = tk.Button(fenetre, text="Inscription", command=Inscription)
Submit.pack()

fenetre.mainloop()

