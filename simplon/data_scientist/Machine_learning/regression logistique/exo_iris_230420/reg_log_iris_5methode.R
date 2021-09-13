#Répartition des données

#Le fractionnement des données implique de partitionner les données en un ensemble de données d'apprentissage explicite utilisé pour préparer le modèle et un ensemble de données de test invisible utilisé pour évaluer les performances du modèle sur des données invisibles.

#Il est utile lorsque vous disposez d'un très grand ensemble de données afin que l'ensemble de données de test puisse fournir une estimation significative des performances, ou lorsque vous utilisez des méthodes lentes et avez besoin d'une approximation rapide des performances.

#L'exemple ci-dessous divise l'ensemble de données iris de sorte que 80% est utilisé pour la formation d'un modèle Naive Bayes et 20% est utilisé pour évaluer les performances du modèle

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

#Le rééchantillonnage bootstrap consiste à prélever des échantillons aléatoires dans l'ensemble de données (avec resélection) par rapport auxquels évaluer le modèle. Globalement, les résultats fournissent une indication de la variance des performances des modèles. En règle générale, un grand nombre d'itérations de rééchantillonnage sont effectuées (des milliers ou des dizaines de milliers).

#L'exemple suivant utilise un bootstrap avec 10 rééchantillons pour préparer un modèle Naive Bayes

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


### Validation croisée k-fold

#La méthode de validation croisée k-fold consiste à diviser l'ensemble de données en k-sous-ensembles. Pour chaque sous-ensemble est maintenu tandis que le modèle est formé sur tous les autres sous-ensembles. Ce processus est terminé jusqu'à ce que la précision soit déterminée pour chaque instance de l'ensemble de données, et une estimation de précision globale est fournie.

#Il s'agit d'une méthode robuste pour estimer la précision, la taille de k et régler la quantité de biais dans l'estimation, avec des valeurs populaires définies sur 3, 5, 7 et 10.

#L'exemple suivant utilise une validation croisée 10 fois pour estimer Naive Bayes sur l'ensemble de données iris

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

### Laissez une validation croisée

#Dans Leave One Out Cross Validation (LOOCV), une instance de données est omise et un modèle est construit sur toutes les autres instances de données de l'ensemble de formation. Cette opération est répétée pour toutes les instances de données.

#L'exemple suivant montre LOOCV pour estimer Naive Bayes sur l'ensemble de données iris
library(caret)
# load the iris dataset
data(iris)
# define training control
train_control <- trainControl(method="LOOCV")
# train the model
model <- train(Species~., data=iris, trControl=train_control, method="nb")
# summarize results
print(model)

### Résumé

#Dans cet article, vous avez découvert 5 méthodes différentes que vous pouvez utiliser pour estimer la précision de votre modèle sur des données invisibles.

#Ces méthodes étaient les suivantes: Data Split, Bootstrap, k-fold Cross Validation, Repeated k-fold Cross Validation et Leave One Out Cross Validation.

#Vous pouvez en savoir plus sur le package du curseur dans R sur la page d'accueil du package du curseur et sur la page CRAN du package du curseur . Si vous souhaitez maîtriser le package caret, je recommanderais le livre écrit par l'auteur du package, intitulé: Applied Predictive Modeling , en particulier le chapitre 4 sur les modèles de sur-ajustement.

