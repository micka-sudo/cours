# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:04:21 2020

@author: Shadow
"""

mdp = input("Entrez un mot de passe (min 8 caractères) : ")


mdp_trop_court = "votre mot de passe est trop court."

if mdp == "0":
   print(mdp_trop_court.upper())
elif len(mdp) < 8:
    print(mdp_trop_court.capitalize())
elif mdp.isnumeric():
    print("Votre mot de passe ne contient que des nombres")
else:
    print("inscription terminée")