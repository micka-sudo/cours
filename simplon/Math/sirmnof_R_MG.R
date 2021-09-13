# Creation des 3 échantillons

x1 <- rnorm(100, mean=0,sd=1)
x2 <- rgamma(100, shape = 1, rate = 0.8)
x3 <- rnorm(50, mean = 10, sd= 5)

# x1 et x2 provienne t'il de la même loi?
ks.test(x1,x2)
  # Pvalues à 1.64 e -12, on rejette l'hypotése nulle
# X1 et X3 proviennent-ils de la même loi ?
ks.test(x1,x3)
  # Pvalues à 2.22 e -16,< alpha on refuse l'hypotése nulle

# X1 provient-il d'une loi gamma avec 3 comme paramètre de forme et 2 pour le taux ? 
ks.test(x1, "pgamma", 3,2)
  #pvalues trés faible on rejette l'hypotése


# X3 provient-il d'une loi normale ? 
ks.test(x3, "pnorm",mean=10,sd=5)

  # Pvalues > alpha on accepte l'hypotése nulle