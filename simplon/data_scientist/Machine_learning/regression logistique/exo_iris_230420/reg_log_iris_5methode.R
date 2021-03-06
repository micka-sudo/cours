#R�partition des donn�es

#Le fractionnement des donn�es implique de partitionner les donn�es en un ensemble de donn�es d'apprentissage explicite utilis� pour pr�parer le mod�le et un ensemble de donn�es de test invisible utilis� pour �valuer les performances du mod�le sur des donn�es invisibles.

#Il est utile lorsque vous disposez d'un tr�s grand ensemble de donn�es afin que l'ensemble de donn�es de test puisse fournir une estimation significative des performances, ou lorsque vous utilisez des m�thodes lentes et avez besoin d'une approximation rapide des performances.

#L'exemple ci-dessous divise l'ensemble de donn�es iris de sorte que 80% est utilis� pour la formation d'un mod�le Naive Bayes et 20% est utilis� pour �valuer les performances du mod�le

# load the libraries
library(caret)
library(klaR)
# load the iris dataset
data(iris)
# define an 80%/20% train/test split of the dataset
split=0.80
trainIndex <- createDataPartition(iris$Species, p=split, list=FALSE)
data_train <- iris[ trainIndex,]
data_test <- iris[-trainIndex,]
# train a naive bayes model
model <- NaiveBayes(Species~., data=data_train)
# make predictions
x_test <- data_test[,1:4]
y_test <- data_test[,5]
predictions <- predict(model, x_test)
# summarize results
confusionMatrix(predictions$class, y_test)


##### BootStrap

#Le r��chantillonnage bootstrap consiste � pr�lever des �chantillons al�atoires dans l'ensemble de donn�es (avec res�lection) par rapport auxquels �valuer le mod�le. Globalement, les r�sultats fournissent une indication de la variance des performances des mod�les. En r�gle g�n�rale, un grand nombre d'it�rations de r��chantillonnage sont effectu�es (des milliers ou des dizaines de milliers).

#L'exemple suivant utilise un bootstrap avec 10 r��chantillons pour pr�parer un mod�le Naive Bayes

# load the library
library(caret)
# load the iris dataset
data(iris)
# define training control
train_control <- trainControl(method="boot", number=100)
# train the model
model <- train(Species~., data=iris, trControl=train_control, method="nb")
# summarize results
print(model)


### Validation crois�e k-fold

#La m�thode de validation crois�e k-fold consiste � diviser l'ensemble de donn�es en k-sous-ensembles. Pour chaque sous-ensemble est maintenu tandis que le mod�le est form� sur tous les autres sous-ensembles. Ce processus est termin� jusqu'� ce que la pr�cision soit d�termin�e pour chaque instance de l'ensemble de donn�es, et une estimation de pr�cision globale est fournie.

#Il s'agit d'une m�thode robuste pour estimer la pr�cision, la taille de k et r�gler la quantit� de biais dans l'estimation, avec des valeurs populaires d�finies sur 3, 5, 7 et 10.

#L'exemple suivant utilise une validation crois�e 10 fois pour estimer Naive Bayes sur l'ensemble de donn�es iris

# load the library
library(caret)
# load the iris dataset
data(iris)
# define training control
train_control <- trainControl(method="cv", number=10)
# fix the parameters of the algorithm
grid <- expand.grid(.fL=c(0), .usekernel=c(FALSE))
# train the model
model <- train(Species~., data=iris, trControl=train_control, method="nb", tuneGrid=grid)
# summarize results
print(model)

### Laissez une validation crois�e

#Dans Leave One Out Cross Validation (LOOCV), une instance de donn�es est omise et un mod�le est construit sur toutes les autres instances de donn�es de l'ensemble de formation. Cette op�ration est r�p�t�e pour toutes les instances de donn�es.

#L'exemple suivant montre LOOCV pour estimer Naive Bayes sur l'ensemble de donn�es iris
library(caret)
# load the iris dataset
data(iris)
# define training control
train_control <- trainControl(method="LOOCV")
# train the model
model <- train(Species~., data=iris, trControl=train_control, method="nb")
# summarize results
print(model)

### R�sum�

#Dans cet article, vous avez d�couvert 5 m�thodes diff�rentes que vous pouvez utiliser pour estimer la pr�cision de votre mod�le sur des donn�es invisibles.

#Ces m�thodes �taient les suivantes: Data Split, Bootstrap, k-fold Cross Validation, Repeated k-fold Cross Validation et Leave One Out Cross Validation.

#Vous pouvez en savoir plus sur le package du curseur dans R sur la page d'accueil du package du curseur et sur la page CRAN du package du curseur . Si vous souhaitez ma�triser le package caret, je recommanderais le livre �crit par l'auteur du package, intitul�: Applied Predictive Modeling , en particulier le chapitre 4 sur les mod�les de sur-ajustement.

