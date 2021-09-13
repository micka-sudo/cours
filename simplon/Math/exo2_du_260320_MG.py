

# 1) De quel type de problème s’agit-il ? 
# Evaluer le procédé de fabrication d'un comprimé à 5 mg de dosage

# 2) Formulez explicitement les hypothèses du test statistique
# H0= Quantité moyenne du principe actif est égale de la moyenne du pcipe actif de l'échantillon
# H1= Quantité moyenne du principe actif est différent de la moyenne du pcipe actif de l'échantillon

# 3) Quel test statistique utilisez vous ? 
# test paramétrique TEST T


# 5) Appliquez le test statistique. 
import numpy as np
from scipy import stats
from math import sqrt

a = 0.05
dosage_reel = 5.0
n = 100
dosage_moyen = 4.85
var = 0.50
ecart = sqrt(var)

pValue = []
for x in range(1000):
    rvs = stats.norm.rvs(loc=dosage_moyen, scale=ecart, size=n)
    test = stats.ttest_1samp(rvs,dosage_reel)
    pValue.append(test[1])

pValues = np.array(pValue)
mean = np.mean(pValues)
if mean > .05:
    print("La quantité de principe actif ne s'approche pas de 5mg u0 !=5.\nL'hypothèse H0 est rejetée.")
else:
    print("La quantité de principe actif s'approche de 5mg.\nL'hypothèse H0 est vraie.")
# np.random.seed(7654567)  # fix seed to get the same result
# rvs = stats.norm.rvs(loc=5, scale=10, size=(50,2))
# stats.ttest_1samp(rvs,5.0)