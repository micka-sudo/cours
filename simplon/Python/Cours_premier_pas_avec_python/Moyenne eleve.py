# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:22:09 2020

@author: Shadow
"""
continuer = True

while continuer:

    Moyenne = int(input("Veuillez entrer votre moyenne :\n"))
    
    if Moyenne < 10:
        print("Vous êtes une gros nul, Vous ne passez pas :\n ")
        if Moyenne >= 10 and Moyenne <= 13:
            print("Vous passez !!!, mais vous n'êtes pas assez fort pour une mention!!!")
            if Moyenne >= 14 and Moyenne <=16:
                print("Vous êtes pas trop mal, vous avez la mention Bien")
                if Moyenne >=17  and Moyenne <= 19:
                    print("Votre Moyenne est de : ", Moyenne, "vous avez la mention Très Bien")
    else:
        print("Votre moyenne est de : ", Moyenne, "Vous avez la mention TOP TOP TOP")
        
        
    Choix = input("Voulez vous rentrer une nouvelle Moyenne ? Si oui tapez oui, et n'importe qu'elle touche pour sortir \n")
    if Choix == ("oui"):
        print("Vous allez rentrez une nouvelle moyenne")
    else:
        continuer = False