# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:04:27 2020

@author: Shadow
"""
liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]

set_liste_01 = set(liste_01)
set_liste_02 = set(liste_02)
intersect = set_liste_01.intersection(set_liste_02)
print(list(intersect))

