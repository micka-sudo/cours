# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:15:29 2020

@author: Shadow
"""

from random import randrange
from math import ceil


def bille_random():
    bille = randrange(0,50)
    print(bille)
    
def numero_joueur():
    try:
        numero = int(input("Veuillez rentrez un nombre entre 0 et 49 : "))
      
        if numero < 0 or numero > 49:
            print("une nombre entre 0 e 49 on a dit !!")
        else:
            print("vous avez jouer le ", numero)
        
    except ValueError:
       print("Veuillez jouer un nombre compris entre 0 et 49")
       
def pot():
    
    try:
        ot = int(input("Veuillez rentrez votre pot de depart compris entre 0 et 10000 Euro")
    
        if pot < 0 or pot > 10000:
            print("Votre pot doit etre compris entre 0 et 10000 euro")
        else:
            print("Vous avez misez", pot)
    except ValueError:
        print("Veuillez rentrez un nombre")   

            
    
           
       
        
