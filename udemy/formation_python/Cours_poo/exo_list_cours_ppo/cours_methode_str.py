
class Voiture:
    def __init__(self, marque, vitesse):
        self.marque = marque
        self.vitesse = vitesse
    # permet de definit l'affichage que l'on veut avoir quand on print notre voiture
    def __str__(self):
        return f"Voiture de marque {self.marque} avec vitesse maximale de {self.vitesse}."


porsche = Voiture("Porsche", 200)
print(porsche)