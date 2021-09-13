import os


dossier_courant = os.path.dirname(__file__)
fichier = os.path.join(dossier_courant, "prenoms.txt")

with open(fichier, "r", encoding="utf-8") as f:
    # fichier_prenoms = f.read()
    # .strip pour effecer . " "  et split pour enlever les ,
    print('\n'.join([prenom.strip() for prenom in f.read().split(",")]))

