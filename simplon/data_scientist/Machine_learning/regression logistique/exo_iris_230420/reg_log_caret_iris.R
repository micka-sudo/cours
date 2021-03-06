data("iris")
iris$Species = as.factor(iris$Species)
head(iris)

library(caret)
library(mlbench)
# choix echantillon al�atoire fixe 
set.seed(12345)

inTrain <- createDataPartition(y = iris$Species, p = .75, list = FALSE)
training <- iris[inTrain,]
testing <- iris[-inTrain,]


#Ensuite, nous devons partitionner les ensembles de formation des ensembles de test. La cr�ation de DataDataPartition dans CARET le fait en prenant un �chantillon al�atoire stratifi� de 0,75 des donn�es pour la formation.

#Nous cr�ons ensuite les ensembles de donn�es de formation et de test qui seront utilis�s pour d�velopper et �valuer le mod�le.

# Ici, nous cr�ons la m�thode de validation crois�e qui sera utilis�e par CARET pour cr�er les ensembles de formation. La validation crois�e signifie de diviser au hasard les donn�es en k (dans notre cas dix) ensembles de donn�es de test de donn�es et la partie r�p�t�e signifie simplement de r�p�ter ce processus k fois (dans notre cas dix �galement).
fitControl <- trainControl(
  method = "repeatedcv",
  number = 10,
  repeats = 10)

#Nous sommes maintenant pr�ts � d�velopper le mod�le. Nous utilisons la fonction train dans CARET pour r�gresser la variable d�pendante Esp�ce sur toutes les autres covariables. Au lieu de nommer explicitement toutes les covariables, dans le package CARET, le �.� Est utilis�, ce qui signifie inclure toutes les autres variables dans l'ensemble de donn�es.
#Ensuite, la m�thode ou le type de r�gression est s�lectionn�. Ici, nous utilisons le gbm ou boosting de gradient stochastique qui est utilis� pour la r�gression et la classification.
library("e1071")
gbmFit1 <- train(Species ~ ., data = training, 
                 method = "gbm", 
                 trControl = fitControl,
                 verbose = FALSE)
#Examinons maintenant les r�sultats. L'information la plus importante est la pr�cision, car c'est ce que CARET utilise pour choisir le mod�le final. Il s'agit du taux d'accord global entre les m�thodes de validation crois�e. Le Kappa est une autre m�thode statistique utilis�e pour �valuer des mod�les avec des variables cat�gorielles telles que la n�tre.

#CARET a choisi le premier mod�le avec une profondeur d'interaction de 1, un nombre d'arbres � 50, une pr�cision de 97% et un Kappa de 95%.

gbmFit1

# Enfin, nous pouvons utiliser le mod�le d'apprentissage pour pr�dire � la fois les classifications et les probabilit�s de l'ensemble de donn�es de test.

#La premi�re ligne de codes utilise la fonction de pr�diction int�gr�e avec le mod�le d'apprentissage (gbmFit1) pour pr�dire les valeurs � l'aide de l'ensemble de donn�es de test, qui repr�sente les 25% de l'ensemble de donn�es que nous avons mis de c�t� au d�but de cet exemple. Nous incluons le code �t�te� pour votre commodit� afin que R n'affiche pas l'ensemble des donn�es. Si �t�te� �tait supprim�e, R afficherait toutes les pr�dictions.

#Le premier morceau de code inclut l'argument type = �prob�, qui indique � R d'afficher les probabilit�s qu'une fleur soit class�e en setosa, versicolor ou virginica. Comme nous pouvons le voir, il y a une probabilit� de 99% que le premier flux de l'ensemble de donn�es soit une setosa.

#Encore une fois, comme indiqu� au d�but de cet exemple, d'autres ensembles de donn�es plus significatifs peuvent �tre substitu�s � l'ensemble de donn�es iris en utilisant les �tapes fournies ci-dessus.

predict(gbmFit1, newdata = head(testing), type = "prob")

