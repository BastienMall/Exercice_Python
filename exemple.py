# Fonction affichage de variable
# 
# nom = "Bastien"
# age= 20
# taille= 1.71
# 
# print(nom)
# print(age)
# print(taille)



# Boucle for
# 
# for i in range(5):
#     print("Répétition n°",i)


# Boucle while
# 
# i = 1
# while i < 11 :
#   if(i % 2 == 0):
#     print(i)
#   i += 1


#  Les listes
# 
# fruits = ["pomme","banane","orange"]
# print(fruits[0])


# def saluer(nom):
# 
#     print("Bonjour"+nom)
# saluer("ALlice")


# Dictionnaire
# 
# personne = {"nom":"Bastien","age":20,"ville":"Asnières"}
# print(personne["nom"])


# Manipulation de chaine de charactère 
# 
# prenom="Bastien"
# nom="MALL"
# nom_complet= prenom + " " + nom
# print(nom_complet)


# Fonction Input
# 
# nom = input("Entre votre nom :")
# print("Bonjour," + nom)

# Utiliser tkinter
import tkinter as tk
# print(tk.TkVersion)

fenetre = tk.Tk()

# fenetre.title("Ma première interface graphique")

# Création d'étiquette
etiquette = tk.Label(fenetre, text="Bravo tu as fait ta première interface graphique")
# permetd'afficher toute les étiquettes
etiquette.pack()

# Création d'un bouton
bouton = tk.Button(fenetre,text="Cliquez sur moi !")
bouton.pack()

fenetre.geometry('400x300')

# permet de rester affiché l'interface jusqu'à ce qu'on clique sur la croix
fenetre.mainloop()