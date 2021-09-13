import numpy as np
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.weightstats import ztest
import pandas as pd
from math import *


# 1) De quel type de problème s’agit-il ? 
# Evaluer le procédé de fabrication d'un comprimé à 5 mg de dosage

# 2) Formulez explicitement les hypothèses du test statistique
# H0= Quantité moyenne du principe actif est égale de la moyenne du pcipe actif de l'échantillon
# H1= Quantité moyenne du principe actif est différent de la moyenne du pcipe actif de l'échantillon

# 3) Quel test statistique utilisez vous ? 
# test paramétrique TEST Z

# 4) Quelles sont les conditions de validité de ce test ? 
# condition de validité

# Si la moyenne est = à la moyenne de l'échantillon, H0 est rejeté
# 5) Appliquez le test statistique. 

count = 5
nobs = 100
value = .05
stat, pval = proportions_ztest(count, nobs, value)
print('{0:0.3f}'.format(pval))

mu = 4.85
var= 0.50
ecarttype = sqrt(var)
a=0.05
mux =5
N=100

stat, pval = proportions_ztest(a, N, mux-mu,prop_var=var)
print(round(1-pval,3))

a = 0.05
dosage_reel = 5
n = 100
dosage_moyen = 4.85
var = 0.50
ecart = sqrt(var)

data = np.random.normal(loc=dosage_moyen, scale=ecart, size=n)

test = ztest(data, value=dosage_reel)
pValue=test[1]

print('p-value = ', pValue)

pValue = []
for x in range(100):
    test = ztest(data, value=dosage_reel)
    pValue.append(test[1])

pValues=np.array(pValue)
print(np.mean(pValues))

# Que concluez-vous ? 
# HO est exclu car la moyenne n'est pas significativement différente.