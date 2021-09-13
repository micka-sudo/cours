
continuer = ()
while continuer != "o":
    prix_ht = input("Veuillez rentrez un prix Ht : \n")
    if prix_ht != "o":
        prix_ttc = int(prix_ht) * 1.19
        print(f" le prix ht est de {prix_ht}, le prix ttc est de : {round(prix_ttc,2)} ")
    
    else:
        print("bye bye")
        break
