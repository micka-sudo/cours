import os
import glob
import json


chemin = r"C:\Users\Shadow\Desktop\Python\formation_udemy\dossier_exemple\**"
dossier = glob.glob(chemin, recursive=True)

numero_compte = None
numero_sec = None

for dos in dossier:
    if dos.endswith(".json"):
        with open(dos, "r") as f:
            contenu = json.load(f)
            if "Credit Mutuel" in contenu:
                numero_compte = contenu["Credit Mutuel"]["Numero de compte"]
                # .get pour eviter  les messaeg d'erreur si pas la clé demandé ds le dico
                # numero_compte = contenu.get("Credit Mutuel","Numero de compte")
    elif dos.endswith(".txt"):
        with open(dos,"r") as t:
            text = t.read()
            if "Numero de securite sociale" in text:
                numero_sec = text.split(":")[-1]

print(numero_compte)
print(numero_sec)

