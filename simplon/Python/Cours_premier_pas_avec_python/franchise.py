# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 19:04:24 2020

@author: Shadow
"""






assurance = 1
while assurance:
    
    Dommage = float(input("Veuillez rentrez le montant de vos dommage : \n"))
    Franchise = Dommage * 0.1
    if Franchise < 15 or Franchise > 500:
        print("Votre franchise doit etre supérieur a 15 ou inferieur a 500")
       
    else:
        print("votre Franchise est de : ", Franchise)
        
    Choix = input("Voulez vous Calculez une autre Franchise ? : Tapez oui pour recalculer \n")
    if Choix == ("oui"):
        print("Bientot un nouveau calcul \n ")
    else:
        print("A bientot dans nos locaux")
        assurance = False
    
       