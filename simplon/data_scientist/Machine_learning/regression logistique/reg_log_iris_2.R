# import data set
library(datasets)
library(ggplot2)
library(gridExtra)
library(grid)
library(plyr)

# load data set
df_iris = iris
#random du data_set
df_iris [sample(nrow(iris),10),]
# Analyse density et fréquences avec hiostogramme

#taille des sepal
HisSl <- ggplot(data=df_iris, aes(x=Sepal.Length))+
  geom_histogram(binwidth=0.2, color="black", aes(fill=Species)) + 
  xlab("Sepal Length (cm)") +  
  ylab("Frequency") + 
  theme(legend.position="none")+
  ggtitle("Histogram of Sepal Length")+
  geom_vline(data=df_iris, aes(xintercept = mean(Sepal.Length)),linetype="dashed",color="grey")

# largeur sepal
HistSw <- ggplot(data=df_iris, aes(x=Sepal.Width)) +
  geom_histogram(binwidth=0.2, color="black", aes(fill=Species)) + 
  xlab("Sepal Width (cm)") +  
  ylab("Frequency") + 
  theme(legend.position="none")+
  ggtitle("Histogram of Sepal Width")+
  geom_vline(data=df_iris, aes(xintercept = mean(Sepal.Width)),linetype="dashed",color="grey")

# taille petal
HistPl <- ggplot(data=df_iris, aes(x=Petal.Length))+
  geom_histogram(binwidth=0.2, color="black", aes(fill=Species)) + 
  xlab("Petal Length (cm)") +  
  ylab("Frequency") + 
  theme(legend.position="none")+
  ggtitle("Histogram of Petal Length")+
  geom_vline(data=df_iris, aes(xintercept = mean(Petal.Length)),
             linetype="dashed",color="grey")

# largeur petal
HistPw <- ggplot(data=df_iris, aes(x=Petal.Width))+
  geom_histogram(binwidth=0.2, color="black", aes(fill=Species)) + 
  xlab("Petal Width (cm)") +  
  ylab("Frequency") + 
  theme(legend.position="right" )+
  ggtitle("Histogram of Petal Width")+
  geom_vline(data=df_iris, aes(xintercept = mean(Petal.Width)),linetype="dashed",color="grey")


# Viz
grid.arrange(HisSl + ggtitle(""),
             HistSw + ggtitle(""),
             HistPl + ggtitle(""),
             HistPw  + ggtitle(""),
             nrow = 2,
             top = textGrob("Iris Frequency Histogram", 
                            gp=gpar(fontsize=15))
            )



DhistPl <- ggplot(df_iris, aes(x=Sepal.Length, colour=Species, fill=Species)) +
  geom_density(alpha=.3) +
  geom_vline(aes(xintercept=mean(Sepal.Length),  colour=Species),linetype="dashed",color="grey", size=1)+
  xlab("Petal Length (cm)") +  
  ylab("Density")+
  theme(legend.position="none")

DhistPw <- ggplot(df_iris, aes(x=Sepal.Width, colour=Species, fill=Species)) +
  geom_density(alpha=.3) +
  geom_vline(aes(xintercept=mean(Sepal.Width),  colour=Species),linetype="dashed",color="grey", size=1)+
  xlab("Petal Width (cm)") +  
  ylab("Density")

DhistSw <- ggplot(df_iris, aes(x=Sepal.Width, colour=Species, fill=Species)) +
  geom_density(alpha=.3) +
  geom_vline(aes(xintercept=mean(Sepal.Width),  colour=Species), linetype="dashed",color="grey", size=1)+
  xlab("Sepal Width (cm)") +  
  ylab("Density")+
  theme(legend.position="none")

DhistSl <- ggplot(df_iris, aes(x=Sepal.Length, colour=Species, fill=Species)) +
  geom_density(alpha=.3) +
  geom_vline(aes(xintercept=mean(Sepal.Length),  colour=Species),linetype="dashed", color="grey", size=1)+
  xlab("Sepal Length (cm)") +  
  ylab("Density")+
  theme(legend.position="none")

grid.arrange(DhistSl + ggtitle(""),
             DhistSw  + ggtitle(""),
             DhistPl + ggtitle(""),
             DhistPw  + ggtitle(""),
             nrow = 2,
             top = textGrob("Iris Density Plot", 
                            gp=gpar(fontsize=15))
)

#Nous pouvons reamarquer que nous avons une ditribustion normal


# Nous pouvons examiner la distribution de densité de chaque attribut, ventilée par valeur de classe.
# Comme la matrice de nuage de points, le diagramme de densité par classe peut aider à voir la séparation des classes.
# Cela peut également aider à comprendre le chevauchement des valeurs de classe pour un attribut.


# Ensuite, avec le bloxplot, nous identifierons certaines valeurs aberrantes. Comme vous pouvez le voir, certaines classes ne se chevauchent pas du tout (par exemple, la longueur des pétales)
# où, comme pour les autres attributs, il est difficile de les distinguer (largeur sépale)
ggplot(iris, aes(Species, Petal.Length, fill=Species)) + 
  geom_boxplot()+
  scale_y_continuous("Petal Length (cm)", breaks= seq(0,30, by=.5))+
  labs(title = "Iris Petal Length Box Plot", x = "Species")


# Tracons toutes les variables dans une seule visualisation qui contiendra tous les boxplots

BpSl <- ggplot(df_iris, aes(Species, Sepal.Length, fill=Species)) + 
  geom_boxplot()+
  scale_y_continuous("Sepal Length (cm)", breaks= seq(0,30, by=.5))+
  theme(legend.position="none")



BpSw <-  ggplot(df_iris, aes(Species, Sepal.Width, fill=Species)) + 
  geom_boxplot()+
  scale_y_continuous("Sepal Width (cm)", breaks= seq(0,30, by=.5))+
  theme(legend.position="none")



BpPl <- ggplot(df_iris, aes(Species, Petal.Length, fill=Species)) + 
  geom_boxplot()+
  scale_y_continuous("Petal Length (cm)", breaks= seq(0,30, by=.5))+
  theme(legend.position="none")



BpPw <-  ggplot(df_iris, aes(Species, Petal.Width, fill=Species)) + 
  geom_boxplot()+
  scale_y_continuous("Petal Width (cm)", breaks= seq(0,30, by=.5))+
  labs(title = "Iris Box Plot", x = "Species")



# Plot all visualizations
grid.arrange(BpSl  + ggtitle(""),
             BpSw  + ggtitle(""),
             BpPl + ggtitle(""),
             BpPw + ggtitle(""),
             nrow = 2,
             top = textGrob("Sepal and Petal Box Plot", 
                            gp=gpar(fontsize=15))
             )


# Vous pouvez également visualiser les données à l'aide des tracés de violon. Ils sont similaires aux Box Box mais ils
# affiche le nombre de points à une valeur particulière par la largeur des formes.
# Le peut également inclure le marqueur de la médiane et une case pour l'intervalle interquartile.

VpSl <-  ggplot(df_iris, aes(Species, Sepal.Length, fill=Species)) + 
  geom_violin(aes(color = Species), trim = T)+
  scale_y_continuous("Sepal Length", breaks= seq(0,30, by=.5))+
  geom_boxplot(width=0.1)+
  theme(legend.position="none")

VpSw <-  ggplot(df_iris, aes(Species, Sepal.Width, fill=Species)) + 
  geom_violin(aes(color = Species), trim = T)+
  scale_y_continuous("Sepal Width", breaks= seq(0,30, by=.5))+
  geom_boxplot(width=0.1)+
  theme(legend.position="none")



VpPl <-  ggplot(df_iris, aes(Species, Petal.Length, fill=Species)) + 
  geom_violin(aes(color = Species), trim = T)+
  scale_y_continuous("Petal Length", breaks= seq(0,30, by=.5))+
  geom_boxplot(width=0.1)+
  theme(legend.position="none")




VpPw <-  ggplot(df_iris, aes(Species, Petal.Width, fill=Species)) + 
  geom_violin(aes(color = Species), trim = T)+
  scale_y_continuous("Petal Width", breaks= seq(0,30, by=.5))+
  geom_boxplot(width=0.1)+
  labs(title = "Iris Box Plot", x = "Species")


# Plot all visualizations
grid.arrange(VpSl  + ggtitle(""),
             VpSw  + ggtitle(""),
             VpPl + ggtitle(""),
             VpPw + ggtitle(""),
             nrow = 2,
             top = textGrob("Sepal and Petal Violin Plot", 
                            gp=gpar(fontsize=15))
)




# Maintenant, créons un diagramme de dispersion des longueurs des pétales par rapport aux largeurs des pétales avec la couleur et la forme par espèce.
# Il existe également une ligne de régression avec une bande de confiance de 95%.
# Remarquez que la longueur des pétales de la setosa est clairement une grappe différenciée, ce sera donc un bon prédicteur pour ML.
# Il existe également une ligne de régression avec une bande de confiance de 95%.
# Il y a aussi une ligne de régression avec une bande de confiance de 95%.

ggplot(data = iris, aes(x = Petal.Length, y = Petal.Width))+
  xlab("Petal Length")+
  ylab("Petal Width") +
  geom_point(aes(color = Species,shape=Species))+
  geom_smooth(method='lm')+
  ggtitle("Petal Length vs Width")

# Voici un graphique similaire avec plus de détails sur la droite de régression.
install.packages("car")
library(car)
scatterplot(iris$Petal.Length,iris$Petal.Width)

# Maintenant, vérifiez la longueur sépale vs largeur. Notez que le sépale des espèces Virginica et Versicolor est plus mélangé, cette caractéristique pourrait ne pas être un bon prédicteur.

ggplot(data=iris, aes(x = Sepal.Length, y = Sepal.Width)) +
  geom_point(aes(color=Species, shape=Species)) +
  xlab("Sepal Length") + 
  ylab("Sepal Width") +
  ggtitle("Sepal Length vs Width")



# Sur la base de toutes les parcelles que nous avons faites, nous pouvons voir qu'il existe une certaine corrélation. Jetons un coup d'oil aux valeurs numériques de corrélation par paire pour
# vérifier les relations plus en détail..
library(GGally)
ggpairs(data = iris[1:4],
        title = "Iris Correlation Plot",
        upper = list(continuous = wrap("cor", size = 5)), 
        lower = list(continuous = "smooth")
)

# L'examen de l'intrigue révèle une forte corrélation entre les variables Largeur du pétale et Longueur du pétale (96%) ainsi que
# La longueur du sépale et la longueur du pétale (87%).



# La heat map est une autre intrigue exploratoire utile. C'est comme un histogramme à deux dimensions et cela fonctionne en utilisant la couleur
# intensité pour représenter la taille de la valeur des données. Plus la couleur est brillante, plus la valeur est élevée.
# Par exemple, la couleur blanche représente la plus grande valeur tandis que le rouge représente la plus petite
# avec des couleurs différentes qui représentent les différentes valeurs entre les deux.

# Créons la matrice et transposons-la avant de l'utiliser pour la heatmap
# assurez-vous que les colonnes correspondent aux caractéristiques et que les lignes correspondent aux observations.
irisMatix <- as.matrix(df_iris[1:150, 1:4])
irisTransposedMatrix <- t(irisMatix)[,nrow(irisMatix):1]

image(1:4, 1:150, irisTransposedMatrix)
