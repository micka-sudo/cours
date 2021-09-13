import random

nombre_mystere = random.randint(0, 10)


compteur = 5

while compteur != 0:
    nombre = input("Quel est le nombre mystère ? ")
    if not nombre.isdigit():
        print("SVP, entrez un nombre valide.")
        continue
    nombre = int(nombre)
    if nombre > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {nombre}")
        compteur -= 1
    elif nombre < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {nombre}")
        compteur -= 1
    else:
        print("Bravo, vous avez trouvé le nombre mystère !")
        exit()
        
print("vous avez perdu")
    
