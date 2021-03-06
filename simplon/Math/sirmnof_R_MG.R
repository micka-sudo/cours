# Creation des 3 �chantillons

x1 <- rnorm(100, mean=0,sd=1)
x2 <- rgamma(100, shape = 1, rate = 0.8)
x3 <- rnorm(50, mean = 10, sd= 5)

# x1 et x2 provienne t'il de la m�me loi?
ks.test(x1,x2)
  # Pvalues � 1.64 e -12, on rejette l'hypot�se nulle
# X1 et X3 proviennent-ils de la m�me loi ?
ks.test(x1,x3)
  # Pvalues � 2.22 e -16,< alpha on refuse l'hypot�se nulle

# X1 provient-il d'une loi gamma avec 3 comme param�tre de forme et 2 pour le taux ? 
ks.test(x1, "pgamma", 3,2)
  #pvalues tr�s faible on rejette l'hypot�se


# X3 provient-il d'une loi normale ? 
ks.test(x3, "pnorm",mean=10,sd=5)

  # Pvalues > alpha on accepte l'hypot�se nulle