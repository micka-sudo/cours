
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Créer trois échantillons 
# X1 de taille 100 qui suit la loi normale centrée réduite
X1 = np.random.normal(0, 1, 100)
plt.hist(np.sort(X1), linewidth=2, color='b')
plt.show()
# X2 de taille 100 qui suit la loi gama(1,0.8)
X2 = np.random.gamma(1, .8, 100)
plt.hist(np.sort(X2), linewidth=2, color='b')
plt.show()
# X3 de taille 50 qui suit la loi normale de moyenne 10 et d’écart-type 5
X3 = np.random.normal(5,10,50)

plt.hist(np.sort(X3), linewidth=2, color='b')
plt.show()
# X1 et X2 proviennent-ils de la même loi ?
print(stats.ks_2samp(X1, X2))

# X1 et X3 proviennent-ils de la même loi ?
print(stats.ks_2samp(X1, X3))
    # Pvalues à 1.08 e -07, on rejette l'hypotése nulle

# X1 provient-il d’une loi gamma avec 3 comme paramètre de forme et 2 pour le taux ? 
print(stats.kstest(X1, 'gamma', args=(3, 2)))
    # Pvalues à 1.08 e -07, on rejette l'hypotése nulle
    
# X3 provient-il d’une loi normale ? 
print(stats.kstest(X3, 'norm', args=(10,5)))
    # Pvalues  > alpha on accepte l'hypotése nulle

"""N = int(input("Enter the size of random numbers to be produced : ")) 
D_plus =[] 
D_minus =[] 
_random =[]
# Rank the N random numbers
for i in range(0, N): 
    _random.append(random.random()) 
    _random.sort() 
  
# Calculate max(i/N-Ri) 
for i in range(1, N + 1): 
    x = i / N - _random[i-1] 
    D_plus.append(x) 
  
# Calculate max(Ri-((i-1)/N)) 
for i in range(1, N + 1): 
    y =(i-1)/N 
    y =_random[i-1]-y 
    D_minus.append(y) 
  
# Calculate max(D+, D-) 
ans = max(max(D_plus, D_minus)) 
print("Value of D is :") 
print(ans) """
