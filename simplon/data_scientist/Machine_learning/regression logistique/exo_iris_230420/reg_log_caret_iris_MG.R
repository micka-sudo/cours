data("iris")
iris$Species = as.factor(iris$Species)
head(iris)

library(caret)
library(mlbench)
# choix echantillon aléatoire fixe 
set.seed(12345)

inTrain <- createDataPartition(y = iris$Species, p = .75, list = FALSE)
training <- iris[inTrain,]
testing <- iris[-inTrain,]


#Ensuite, nous devons partitionner les ensembles de formation des ensembles de test. La création de DataDataPartition dans CARET le fait en prenant un échantillon aléatoire stratifié de 0,75 des données pour la formation.

#Nous créons ensuite les ensembles de données de formation et de test qui seront utilisés pour développer et évaluer le modèle.

# Ici, nous créons la méthode de validation croisée qui sera utilisée par CARET pour créer les ensembles de formation. La validation croisée signifie de diviser au hasard les données en k (dans notre cas dix) ensembles de données de test de données et la partie répétée signifie simplement de répéter ce processus k fois (dans notre cas dix également).
fitControl <- trainControl(
  method = "repeatedcv",
  number = 10,
  repeats = 10)

#Nous sommes maintenant prêts à développer le modèle. Nous utilisons la fonction train dans CARET pour régresser la variable dépendante Espèce sur toutes les autres covariables. Au lieu de nommer explicitement toutes les covariables, dans le package CARET, le «.» Est utilisé, ce qui signifie inclure toutes les autres variables dans l'ensemble de données.
#Ensuite, la méthode ou le type de régression est sélectionné. Ici, nous utilisons le gbm ou boosting de gradient stochastique qui est utilisé pour la régression et la classification.
library("e1071")
gbmFit1 <- train(Species ~ ., data = training, 
                 method = "gbm", 
                 trControl = fitControl,
                 verbose = FALSE)
#Examinons maintenant les résultats. L'information la plus importante est la précision, car c'est ce que CARET utilise pour choisir le modèle final. Il s'agit du taux d'accord global entre les méthodes de validation croisée. Le Kappa est une autre méthode statistique utilisée pour évaluer des modèles avec des variables catégorielles telles que la nôtre.

#CARET a choisi le premier modèle avec une profondeur d'interaction de 1, un nombre d'arbres à 50, une précision de 97% et un Kappa de 95%.

gbmFit1

# Enfin, nous pouvons utiliser le modèle d'apprentissage pour prédire à la fois les classifications et les probabilités de l'ensemble de données de test.

#La première ligne de codes utilise la fonction de prédiction intégrée avec le modèle d'apprentissage (gbmFit1) pour prédire les valeurs à l'aide de l'ensemble de données de test, qui représente les 25% de l'ensemble de données que nous avons mis de côté au début de cet exemple. Nous incluons le code «tête» pour votre commodité afin que R n'affiche pas l'ensemble des données. Si «tête» était supprimée, R afficherait toutes les prédictions.

#Le premier morceau de code inclut l'argument type = «prob», qui indique à R d'afficher les probabilités qu'une fleur soit classée en setosa, versicolor ou virginica. Comme nous pouvons le voir, il y a une probabilité de 99% que le premier flux de l'ensemble de données soit une setosa.

#Encore une fois, comme indiqué au début de cet exemple, d'autres ensembles de données plus significatifs peuvent être substitués à l'ensemble de données iris en utilisant les étapes fournies ci-dessus.

predict(gbmFit1, newdata = head(testing), type = "prob")

