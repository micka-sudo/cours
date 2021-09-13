#       _ _,---._
#    ,-','       `-.___
#   /-;'               `._
#  /\/          ._   _,'o \
# ( /\       _,--'\,','"`. )
#  |\      ,'o     \'    //\
#  |      \        /   ,--'""`-.
#  :       \_    _/ ,-'         `-._
#   \        `--'  /                )
#    `.  \`._    ,'     ________,','
#      .--`     ,'  ,--` __\___,;'
#       \`.,-- ,' ,`_)--'  /`.,'
#        \( ;  | | )      (`-/
#          `--'| |)       |-/
#            | | |        | |
#            | | |,.,-.   | |_
#            | `./ /   )---`  )
#           _|  /    ,',   ,-'
#  -hrr-   ,'|_(    /-<._,' |--,
#          |    `--'---.     \/ \
#          |          / \    /\  \
#        ,-^---._     |  \  /  \  \
#     ,-'        \----'   \/    \--`.
#    /            \              \   \
# class Voiture:
#     marque = "Lamborghini"
#     couleur = "rouge"


# voiture_01 = Voiture()
# print(voiture_01.marque)

# Voiture.marque = "Porche"
# print(voiture_01.marque)

# voiture_02 = Voiture()
# voiture_02.marque = "Renault"
# print(voiture_02.marque)

# Méthode init:


# class Voiture:
#     voiture_crees = 0
#     def __init__(self, marque):
#         Voiture.voiture_crees += 1
#         self.marque = marque

# voiture_01 = Voiture("Porsche")
# voiture_02 = Voiture("Renault")
# print(voiture_01.marque)
# print(voiture_02.marque)
# print(Voiture.voiture_crees)

class Livre:
    def __init__(self, nom, nombre_de_pages, prix):
        self.nom = nom
        self.nombre_de_pages = nombre_de_pages
        self.prix = prix

livre_HP = Livre("Harry Potter", 300, 10.99)
livre_LORT = Livre("Le seigeneur des Anneaux", 400, 13.99)
print(livre_LORT.prix)