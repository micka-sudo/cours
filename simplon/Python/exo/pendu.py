# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 12:01:19 2020

@author: Shadow
"""

from random import *

print("======== bienvenue au jeux du pendu promo dataIa=====")


    
#motRandom = len(motRandom)
mot = ["carotte","choux","navets","bannanes"]                            
motRandom = sample(mot,1)[0]
chance = 9

while chance != 0: 
    
    print("Vous devez chercher un mot de", len(motRandom), "lettres : \n")
    mot_a_trouver = list("-"*len(motRandom))
    #mot_a_trouver = "".join(mot_a_trouver)    
        
    print(mot_a_trouver)
    print(motRandom)
    
    lettreJouer = input("Veuillez rentrez une lettre : \n")
    
    if lettreJouer in motRandom:
        for (index, value) in enumerate(motRandom):
            if value == lettreJouer:
                mot_a_trouver[index] = value
        mot_trouver = "".join(mot_a_trouver)
        print("bravo ", mot_trouver)
    
    else:
        
        chance -= 1
        print("dtc", chance)
        break
