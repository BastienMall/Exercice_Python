# Créez une calculatrice simple en Python qui permet à l'utilisateur d'effectuer des opérations de base (addition, soustraction, multiplication et division).
# Utiliser un if pour déterminer quels opé faire
# et créer une fonction addition(n1, n2) qui renvoie une somme de n1 et n2

import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Exo3 - Calculatrice")
fenetre.geometry("1000x500")

Nombre1Etiquette = tk.Label(fenetre, text="Indiquez un premier nombre")
Nombre1Champ = tk.Entry(fenetre)
Nombre1Etiquette.pack()
Nombre1Champ.pack()

OperateurEtiquette = tk.Label(fenetre, text="Séléctionner un opérateur")
# OperateurBox = tk.Combobox(fenetre, values=["+", "-", "/", "x"])
OperateurEtiquette.pack()
# OperateurBox.pack()

Nombre2Etiquette = tk.Label(fenetre, text="Indiquez un deuxième nombre")
Nombre2Champ = tk.Entry(fenetre)
Nombre2Etiquette.pack()
Nombre2Champ.pack()

def Calcul() :
    print()

Submit = tk.Button(fenetre, text="Inscription", command=Calcul)
Submit.pack()

fenetre.mainloop()