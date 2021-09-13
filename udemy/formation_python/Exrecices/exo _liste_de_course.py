import os
import json

dossier_courant = os.path.dirname(__file__)
# concaténation dossier courant et liste_course.json
dir_list = os.path.join(dossier_courant, "liste_course.json")

# Vérifie si dir_list existe
if os.path.exists(dir_list):
    # si oui ouvre le fichier.
    with open(dir_list,"r") as l:
        course = json.load(l)
# Si non crée une list course vide.
else:
    course = []

affichage = """
Choisissez une choix:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Terminer
"""
choix = True
while choix:
    choix = input(affichage)
    if choix != "5":
        if choix == "1":
            ajout = input("Veuillez entrez l'élément à ajouter : \n")
            course.append(ajout)
        elif choix == "2":
            enlever = input("quel éléménent voulez vous enlevez ? : \n")
            if enlever in course:
                course.remove(enlever)
        elif choix == "3":
            if course:
                for i in course:
                    print(i)
        elif choix == "4":
            course.clear()
            
    else:
        choix = False

with open(dir_list,"w") as w:
    json.dump(course, w, indent=4)

# autre facon pour boucler

# choix = "0"
# while choix != "5":
#     choix = input(affichage)

# autre facon de mettre la liste à la ligne
# elif choix == "3":
#             print("\n".join(course))