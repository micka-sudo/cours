class Voiture:
    voiture_crees = 0
    def __init__(self, marque, vitesse, prix):
        Voiture.voiture_crees += 1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    # la methode classe n'impartient pas aux instance ms appartient a la classe
    @classmethod
    #  en parametre par convention cls = class
    #  methode de classe pour eviter de ce rapelé les element de notre voiture
    def lamborghini(cls):
        return cls(marque="Lamborghini", vitesse=250, prix=200000)

    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse=200, prix=180000)

    #  Permet de ce servir de voiture_crees sans argument(utile quand pas d'obligation a etre associer a des instance ou pas de manip direct sur le classe )
    @staticmethod
    def afficher_nombre_voitures():
        print(f"Vous avez {Voiture.voiture_crees} voitures dans votre garage.")

lambo = Voiture.lamborghini()
porsche = Voiture.porsche()
Voiture.afficher_nombre_voitures()