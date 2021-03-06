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
# Analyse density et fr�quences avec hiostogramme

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


# Nous pouvons examiner la distribution de densit� de chaque attribut, ventil�e par valeur de classe.
# Comme la matrice de nuage de points, le diagramme de densit� par classe peut aider � voir la s�paration des classes.
# Cela peut �galement aider � comprendre le chevauchement des valeurs de classe pour un attribut.


# Ensuite, avec le bloxplot, nous identifierons certaines valeurs aberrantes. Comme vous pouvez le voir, certaines classes ne se chevauchent pas du tout (par exemple, la longueur des p�tales)
# o�, comme pour les autres attributs, il est difficile de les distinguer (largeur s�pale)
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


# Vous pouvez �galement visualiser les donn�es � l'aide des trac�s de violon. Ils sont similaires aux Box Box mais ils
# affiche le nombre de points � une valeur particuli�re par la largeur des formes.
# Le peut �galement inclure le marqueur de la m�diane et une case pour l'intervalle interquartile.

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




# Maintenant, cr�ons un diagramme de dispersion des longueurs des p�tales par rapport aux largeurs des p�tales avec la couleur et la forme par esp�ce.
# Il existe �galement une ligne de r�gression avec une bande de confiance de 95%.
# Remarquez que la longueur des p�tales de la setosa est clairement une grappe diff�renci�e, ce sera donc un bon pr�dicteur pour ML.
# Il existe �galement une ligne de r�gression avec une bande de confiance de 95%.
# Il y a aussi une ligne de r�gression avec une bande de confiance de 95%.

ggplot(data = iris, aes(x = Petal.Length, y = Petal.Width))+
  xlab("Petal Length")+
  ylab("Petal Width") +
  geom_point(aes(color = Species,shape=Species))+
  geom_smooth(method='lm')+
  ggtitle("Petal Length vs Width")

# Voici un graphique similaire avec plus de d�tails sur la droite de r�gression.
install.packages("car")
library(car)
scatterplot(iris$Petal.Length,iris$Petal.Width)

# Maintenant, v�rifiez la longueur s�pale vs largeur. Notez que le s�pale des esp�ces Virginica et Versicolor est plus m�lang�, cette caract�ristique pourrait ne pas �tre un bon pr�dicteur.

ggplot(data=iris, aes(x = Sepal.Length, y = Sepal.Width)) +
  geom_point(aes(color=Species, shape=Species)) +
  xlab("Sepal Length") + 
  ylab("Sepal Width") +
  ggtitle("Sepal Length vs Width")



# Sur la base de toutes les parcelles que nous avons faites, nous pouvons voir qu'il existe une certaine corr�lation. Jetons un coup d'oil aux valeurs num�riques de corr�lation par paire pour
# v�rifier les relations plus en d�tail..
library(GGally)
ggpairs(data = iris[1:4],
        title = "Iris Correlation Plot",
        upper = list(continuous = wrap("cor", size = 5)), 
        lower = list(continuous = "smooth")
)

# L'examen de l'intrigue r�v�le une forte corr�lation entre les variables Largeur du p�tale et Longueur du p�tale (96%) ainsi que
# La longueur du s�pale et la longueur du p�tale (87%).



# La heat map est une autre intrigue exploratoire utile. C'est comme un histogramme � deux dimensions et cela fonctionne en utilisant la couleur
# intensit� pour repr�senter la taille de la valeur des donn�es. Plus la couleur est brillante, plus la valeur est �lev�e.
# Par exemple, la couleur blanche repr�sente la plus grande valeur tandis que le rouge repr�sente la plus petite
# avec des couleurs diff�rentes qui repr�sentent les diff�rentes valeurs entre les deux.

# Cr�ons la matrice et transposons-la avant de l'utiliser pour la heatmap
# assurez-vous que les colonnes correspondent aux caract�ristiques et que les lignes correspondent aux observations.
irisMatix <- as.matrix(df_iris[1:150, 1:4])
irisTransposedMatrix <- t(irisMatix)[,nrow(irisMatix):1]

image(1:4, 1:150, irisTransposedMatrix)
