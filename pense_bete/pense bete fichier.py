
chemin = "/Users/desk/fichier.txt"

# on ne peut pas ouvrir un .Json vide
# ensure_ascii à False pour paramétré corectement les accents^^
# .seek() permet de mettre le curseur ou l'on veut .seek(0), .seek(10) ect....
# with permet de lire nu fichier et de le refermer
with open(chemin, "r") as f: # "r" = read
    # .read pour lire un fichier
    contenue = f.read()
    # repr permet d'acceder à la représentation de chaine de caractére
    contenue = repr(f.read())
    # Permet de creer une liste en récupérent tout les éléments
    contenue = f.readlines()
    # Récupérer chaque ligne sans \n
    contenue = f.read().splitlines()
    print(contenu)

###########################
#Ecrire dans un fichier
###########################
with open(chemin, "w") as f: # "w" réecrit sur le fichier "a" append rajoute au fichier.

##########################
#Fichier Json
##########################

import json

with open(chemin, "w") as f:
    json.dump("Bonjour", f) # .dump, ce qu'on veut ecrire à l'intérieur du fichier
    json.dump(list(range(10)), f indent= 4) # indent permet de choisir son indentation
    liste = json.load(f) # pour charger un fichier en mode read "r"