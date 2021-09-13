# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:42:50 2020

@author: Shadow
"""

# exo 1 Ecrire un programme qui etant donnée 2 borne a et b, additione les nbr multipe de 3 et 5

a = 0
b = 32

somme = 0
for nombre in range(a, b):
    
    if nombre % 3 == 0 and nombre % 5 == 0:       
        somme += nombre
print(somme)


# exo 1 suite

somme2 = 0
for nombre in  range(a, b):
    if nombre % 3 == 0 or nombre % 5 == 0:
        somme2 += nombre
print(somme2)
