# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:10:19 2020

@author: Shadow
"""

import random

nombre_mystere = random.randint(0, 10)
nombre = input("Quel est le nombre mystère ? ")
if not nombre.isdigit():
    print("SVP, entrez un nombre valide.")
    exit()

nombre = int(nombre)
if nombre > nombre_mystere:
    print(f"Le nombre mystère est plus petit que {nombre}")
elif nombre < nombre_mystere:
    print(f"Le nombre mystère est plus grand que {nombre}")
elif nombre != nombre.isdig    
else:
    print("Bravo, vous avez trouvé le nombre mystère !")