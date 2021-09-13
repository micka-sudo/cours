# import data set
library(datasets)

df_iris<- iris
head(df_iris)
str(df_iris)

# les palantes dans spécies

levels(df_iris$Species)

# check des valeur null
sum(is.na(ir_data))

df_iris <- df_iris[1:100,]

# creation en random goupe test et de control
set.seed(100)
rand <- sample(1:100,80)
df_test <- df_iris[rand,]
df_ctrl <- df_iris[rand,]

# import des library pour les test

library(ggplot2); library(GGally)
# pour obtenir un aprecu de nos données et pour avoir les corrélaiton entre les variabes
# ggpairs donne une meilleur compréhension que paires
#pairs(df_iris)
ggpairs(df_iris)

# modelisation donnée avec reg log

y<-df_iris$Species; x<-df_iris$Sepal.Length
glfit<-glm(y~x, family = 'binomial')
# on utilise  logit pour determiné la probalité si une plante sera satosa ou versicolor
# en fonction de ca longueur de petal
# calcul des median min ect....
summary(glfit)
newdata<- data.frame(x=df_ctrl$Sepal.Length)
predicted_val<-predict(glfit, newdata, type="response")
prediction<-data.frame(df_ctrl$Sepal.Length, df_ctrl$Species,predicted_val)
prediction
# parcequ'un petit graph sera ca fait toujours plaisir
qplot(prediction[,1], round(prediction[,3]), col=prediction[,2], xlab = 'Sepal Length', ylab = 'Prediction using Logistic Reg.')

