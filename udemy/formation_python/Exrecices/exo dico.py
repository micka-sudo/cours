# employes = {
#             "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
#             "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
#             "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
#             }

# del employes["id03"]
# employes["id02"]["age"] = 26
# age_paul = employes["id01"]["age"]
# print(employes)
# print(age_paul)


# Créer une structure de dossiers :

import os

chemin = r"C:\Users\Shadow\Desktop\Python\formation_udemy"

d = {"Films": ["babar à la plage", "babar à ma montagne", "oui oui fait du ski"],
     "Employés": ["babar", "oui oui", "clara morgane"],
     "Exrecices": ["boucle", "dico", "variable"]}

for key, value in d.items():
    for dossier in value:
        dir_chemin = os.path.join(chemin, key, dossier)
        os.makedirs(dir_chemin, exist_ok=True)
