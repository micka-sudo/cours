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
#######################################
#                Gruy                 #                  
#######################################

class Voiture:
    def __init__(self):
        self.essence = 100

    def afficher_essence(self):
        print(f"Il vous reste {self.essence} L d'essence.")

    def roule(self, km):
        
        if self.essence <= 0:
            print("passse à la pompe boulet tu n'a plus d'essence")
            return

        self.essence -= (km*5) / 100

        if self.essence < 10:
            print(f"Il vous reste {self.essence}, Allez faire le plein ")
        else:
            print(f"Il vous reste {self.essence}")

    def faire_le_plein(self):
        self.essence = 100
        print("Vous avez fait le plein, go sur les routes")

porsche = Voiture()
porsche.afficher_essence()
porsche.roule(1850)





