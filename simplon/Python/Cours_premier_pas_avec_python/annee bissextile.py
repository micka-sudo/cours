# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 20:40:15 2020

@author: Shadow
"""

# Calcule pour savoir si l'anneé est biisextile ou pas

"""annee = int(input("Veuillez entrer votre année pour savoir si elle est bissextile ou pas : \n"))


if annee % 4 == 0:
    print("l'année ", annee, "est bissextille")
    if annee % 100 == 0:
        print("l'année ", annee, "n'est pas bissextille")
        if annee % 400 != 0:
            print("l'année ", annee, "est bissextille")
else:
    print("l'année ", annee, "n'est pas bissextille")"""
    
    

listeEntier = input("Veuillez rentrez une liste de nombre separer par des virgule :")

liste = listeEntier.split(',')

print(" votre liste en colonne")

for nbre in liste:
    
    print(nbre)
print("--------------")

print("liste inverser")
liste.reverse()
print(liste)
print("----------------")

print("compter le nombre multi de 3 dans la liste")

nbreMulti = 0
for multi in liste:
    if int(multi) % 3 == 0:
        nbreMulti += 1
print(nbreMulti)
        
print("--------------------")

nbrePaire = 0
for nbre in liste:
    if int(nbre) % 2 == 0:
        nbrePaire += int(nbre)
print(nbrePaire)
    



