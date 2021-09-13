# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 21:40:55 2020

@author: Shadow
"""

"""a = int(input("veuillez rentre la 1er borne: "))
b = int(input("veuillez rentre la 2eme borne: "))

retenu = []


for i in range (a,b):
    if i % 3 == 0 and i % 5 == 0:
        retenu.append(i)


resultat = 0

for  somme in retenu:
    resultat += somme
print("le resultat est :", resultat)"""

"""a = int(input("veuillez rentrez la 1er borne : "))
b = int(input("veuillez rentrez la 2 éme borne : "))

retenu = []

for i in range (a, b):
    if i % 3 == 0 or i % 5 == 0:
        retenu.append(i)

resultat = 0
for y in retenu:
    resultat += y
print(" le resultat est ", resultat)"""

annee = int(input(" Veuillez rentrez une année pour savoir si elle est bisssextil : \n"))

if annee % 4 == 0:
    print(annee, " est bissextille")
elif annee % 100 == 0:
        print(annee, "n'est pas bissextille")
elif annee % 400 != 0:
        print(annee, " est bissextille")
else:
    print(annee, "n'est pas bissextille")