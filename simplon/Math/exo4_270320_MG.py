
from scipy.stats import f
import matplotlib.pyplot as plt
import numpy as np
# De quel type de problème s’agit-il ? 
#  Toujours pareil un probléme relou
# Formulez explicitement les hypothèses du test statistique
#  Si Ho est accépté si var1 =var2
#  Si H1 est rejété si var1 > var2
# Quel test statistique utilisez vous ? 
# Test de Ficher
# Quelles sont les conditions de validité de ce test ? 
#   𝑥_1  ~𝑁(𝜇_1,𝜎_1) et 𝑥_(2 )~𝑁(𝜇_2,𝜎_2)


# Appliquez le test statistique. 

mu1 = 107
sigma1=10
n1= 9
var1= sigma1**2
mu2=112
sigma2 = 9
n2=12
var2= sigma2**2
alpha = .05

df1, df2 = n1-1, n2-1
F = sigma1 / sigma2
p_value = f.cdf(F, df1, df2)

fig, ax = plt.subplots(1, 1)

mean, var, skew, kurt = f.stats(df1, df2, moments='mvsk')
print("mean = ", mean)
print("var =", var)
print("skew =", skew)
print("kurt = ", kurt)

x = np.linspace(f.ppf(0.01, df1, df2),
               f.ppf(0.99, df1, df2), 100)
ax.plot(x, f.pdf(x, df1, df2),
       'r-', lw=5, alpha=0.6, label='test')

rv = f(df1, df2)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='loi ficher')


vals = f.ppf([0.001, 0.5, 0.999], df1, df2)
np.allclose([0.001, 0.5, 0.999], f.cdf(vals, df1, df2))

r = f.rvs(df1, df2, size=1000)

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)


# Que concluez-vous ?

if p_value < alpha:
    print('H0 rejeté')
else:
    print('H0 est accépté')

plt.show()