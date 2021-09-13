import os


chemin = r"C:\Users\Shadow\Desktop\Python\formation_udemy\exo_structure_dossier"

d = {"Films": ["Le seigneur des anneaux",
			   "Harry Potter",
			   "Moon",
			   "Forrest Gump"],
	 "Employes": ["Paul",
	 		      "Pierre",
				  "Marie"],
	 "Exercices": ["les_variables",
	 			   "les_fichiers",
				   "les_boucles"]}

for key in d:
    if not os.path.exists(os.path.join(chemin, key)):
        os.mkdir(os.path.join(chemin, key))
    for contenu in d[key]:
        if not os.path.exists(os.path.join(chemin, key, contenu)):
            os.mkdir(os.path.join(chemin, key, contenu))

# autre soluce

"""for key, value in d.items():
        for dossier in values:
            chemin_dossier = os.path.join(chemin, key, dossier):
            os.makedirs(chemin_dossier, exist_ok=True)"""