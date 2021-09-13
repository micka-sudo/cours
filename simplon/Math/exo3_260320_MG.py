import numpy as np
from scipy import stats
from math import sqrt

# De quel type de problème s’agit-il ? 
# un probléme relou
# Formulez explicitement les hypothèses du test statistique
#  H0 = H1 La pression arterielle systolique mesurée à l'âge de 7 ans diffère dû à l'allaitement maternel à la naissance.\nL'hypothèse H0 est rejetée.
#  H0 != H1 La pression arterielle systolique mesurée à l'âge de 7 ans ne diffère pas en fonction de l'allaitement maternel à la naissance.\nL'hypothèse H0 est vraie
# Quel test statistique utilisez vous ? 
#  Test Z
# Quelles sont les conditions de validité de ce test ? 


# Appliquez le test statistique. 
a= 0.05
mu1 = 98.5
sigma1=9.0
n1= 5478
mu2=99.99
sigma2 = 9.6
n2=1125



Z = (mu1-mu2)/sqrt((sigma1**2/n1)+(sigma2**2/n2))
print(Z)

pvalue = []

# essaye avec numpy
"""for i in range(100):
    data = np.random.normal(loc=mu1, scale=sigma1, size=n1)
    data2 = np.random.normal(loc=mu2, scale=sigma2, size=n2)
    test_T = stats.ttest_ind(data,data2, equal_var=False)
    pvalue.append(test_T[1])"""
# essaye avec spicy
for i in range(100):
    data1 = stats.norm.rvs(loc=mu1,scale=sigma1,size=n1)
    data2 = stats.norm.rvs(loc=mu2,scale=sigma2,size=n2)
    test_T = stats.ttest_ind(data1, data2, equal_var=False)
    pvalue.append(test_T[1])

pvalues = np.array(pvalue)
mean = np.mean(pvalue)
print (mean)
T = np.mean(data1)
c = T*0.975
d = 1 - c
print("pvalue :", mean, "Z-mean", T)
print("W = ]-inf;", c, "]U[", d, ";+inf[")


# Que concluez-vous ?
if mean < a:
    print("L'hypothèse H0 est rejetée.La pression arterielle systolique mesurée à l'âge de 7 ans n'a pas d'influence en fonction de l'allaitement maternel à la naissance.\nL'hypothèse H0 est vraie.")
else:
    print("La pression arterielle systolique mesurée à l'âge de 7 ans a une influence dû à l'allaitement maternel à la naissance.\n")



