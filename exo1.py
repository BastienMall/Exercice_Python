# Créer un programme qui permet à l'utilisateur de saisir et de gérer des informations personnelles telles que le nom, l'âge, la taille, la liste des fruits préférés, un message de salutation personnalisé, les propriétés d'un produit, la manipulation de chaînes de caractères et l'entrée de l'utilisateur.
# Nom de famille en maj


nom = input("Entrez votre nom:")
age= input("Entrez votre age:")
taille= input("Entrez votre taille:")

fruits=input("Entrez votre fruits préféré:")



print("Bonjour " + nom.upper()+ ", votre age est "+ age + ", votre taille est de " + taille + " mètre " + "et vos fruits préféré sont " + fruits )