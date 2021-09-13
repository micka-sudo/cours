import logging
import json
import os
# import du fichier constant que j'ai creer pour les chemin absolue
from constant import DATA_DIR

LOGGER = logging.getLogger()

class Liste(list):
    def __init__(self, nom):
        self.nom = nom

    def ajouter(self, elememt):
        #  si element n'est pas de type string raise(levée)
        if not isinstance(elememt, str):
            raise ValueError("Vous ne pouvea ajouter que des chaines de caractéres!")

        if elememt in self:
            #  LOGGER permet de generer des type d'erreur
            LOGGER.error(f"{elememt} est déja dans la liste.")
            return False

        self.append(elememt)
        return True

    def enlever(self, elememt):
        if elememt in self:
            self.remove(elememt)
            return True
        return False

    def afficher(self):
        print(f"Ma liste de {self.nom} :")
        for element in self:
            print(f" - {element}")

    def sauvegarder(self):
        chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        # verification si le fichier exist ou pas
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        with open(chemin, "w") as f:
            json.dump(self, f, indent=4)

        return True

if __name__ == "__main__":
    liste = Liste("course")
    
    liste.ajouter("pommes")
    liste.ajouter("poire")
    liste.sauvegarder()
    liste.afficher()

