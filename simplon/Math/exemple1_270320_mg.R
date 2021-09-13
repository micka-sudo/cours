y <- c(11, 27, 29, 20, 11, 1, 1)
z<- sum(y)


lambda = sum((0:6) * y) / z
lambda


proba = c(dpois(0:5, lambda), 1 - ppois(5, lambda))
proba
barplot(proba)
chisq.test(y, p = proba)$p.value
# On accepte H0. Les valeurs suivent donc une loi de poisson.