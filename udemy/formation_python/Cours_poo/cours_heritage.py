projets = ["pr_GameOfThrones", "HarryPotter", "pr_Avengers"]


class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"Utilisateur {self.nom} {self.prenom}"

    def afficher_projets(self):
        for projet in projets:
            print(projet)

# Junior hérite de la classe utilisateur
class Junior(Utilisateur):
    # récupére le nom prenom comme dans la class utilisateur
    def __init__(self, nom, prenom):
        # initialisation de la class utilisateur dans junior
        Utilisateur.__init__(self, nom, prenom)

        

paul = Junior("Paul", "Durand")
print(paul)