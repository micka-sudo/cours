import os
import glob
import shutil
import json


"""# Creation du chemin d'accés
chemin = r"C:\Users\Shadow\Desktop\Python\formation_udemy\tri_fichiers_sources\**"

# Création variable pour lire tout les chiffiers du dossier.
dossier = glob.glob(chemin, recursive=True)

# Création chemin replace pour la creation de mes différent dossier.
chemin = chemin.replace("**","")

# creation de mes différent dossier os.makedirs(chemin, exist_ok= True) pour verifier que le fichier est créé ou pas False, evite message d'erreur
chemin_image = os.path.join(chemin, "Images")
os.makedirs(chemin_image, exist_ok=True)
chemin_video = os.path.join(chemin, "Video")
os.makedirs(chemin_video, exist_ok=True)
chemin_dossier = os.path.join(chemin, "Dossier")
os.makedirs(chemin_dossier, exist_ok=True)
chemin_musique = os.path.join(chemin, "Musiques")
os.makedirs(chemin_musique, exist_ok=True)
chemin_json = os.path.join(chemin, "Json")
os.makedirs(chemin_json, exist_ok=True)

for fichier in dossier:
    if fichier.endswith(".jpg") or fichier.endswith('png'):
        shutil.move(fichier, chemin_image)
    elif fichier.endswith("mp4") or fichier.endswith("mov"):
        shutil.move(fichier, chemin_video)
    elif fichier.endswith("pdf"):
        shutil.move(fichier, chemin_dossier)
    elif fichier.endswith('mp3') or fichier.endswith('wav'):
        shutil.move(fichier,chemin_musique)
    elif fichier.endswith('.json'):
        shutil.move(fichier, chemin_json)"""


# Corrigé exo

from glob import glob
chemin = r"C:\Users\Shadow\Desktop\Python\formation_udemy\tri_fichiers_sources"
extensions = {".mp3": "Musique",
              ".wav": "Musique",
              ".mp4": "Videos",
              ".mov": "Videos",
              ".jpeg": "Images",
              ".jpg": "Images",
              ".png": "Images",
              ".pdf": "Documents"}

fichiers = glob(os.path.join(chemin, "*"))
for fichier in fichiers:
    # split les fichiers pour garder la derniére parti [-1] .XXX
    extension = os.path.splitext(fichier)[-1]
    # indique la key au dictionnaire extensions.get(".XXX")
    dossier = extensions.get(extension)
    #condition création dossier et vérification
    if dossier:
        chemin_dossier = os.path.join(chemin, dossier)
        os.makedirs(chemin_dossier, exist_ok=True)
        shutil.move(fichier, chemin_dossier)