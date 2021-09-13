
import os

# C:/Users/Shadow/Desktop/Python/formation_udemy/Exo_gestion_des_erreurs/readme.txt
# C:/Users/Shadow\Desktop/Python/formation_udemy/Exo_gestion_des_erreurs/fichier_invalide.abc


choix_fichier = input("Veuillez copiez le liens de voitre fichier à ouvrir : \n")

try:
    with open(choix_fichier, "r") as fichier:
        print(fichier.read())
# gestion erreur fichier present ou pas
except FileNotFoundError:
    print("Fichier non trouvé")
#  gestion erreur type de fichier
except UnicodeDecodeError:
    print("impossible d'ouvrier le fichier")






