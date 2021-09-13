# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:51:23 2020

@author: Shadow
"""

# exo 1 pour l'instruction for

"""nom = ['D', 'A', 'E', 'U', '-', 'B', '\n']

for lettre in nom:
    print(lettre)
    
# exo 2 pour l'instruction for
    
    
for entier in range(0,15):
    if entier % 3 == 0:
        print(entier, "\n")
    
    
# exo 3 pour l'instruction for

for entier in range(1,11):
    if entier % 2 == 0:
        print(entier, "\n")
    else:
        if entier == 5:
            break
        
# exo 4 pour l'instruction for (ne fonctionne pas)
            
for entier in range(1, 11):
    if entier == 5:
        continue
        print(entier)"""
        

# exo 5 pour l'instrucion for 
nombre = input("Veuillez entrer une nombre entier pour calculer son factoriel: \n")
nombre = int(nombre)


for i in range(1, nombre):
    nombre *= i
print(nombre)
    