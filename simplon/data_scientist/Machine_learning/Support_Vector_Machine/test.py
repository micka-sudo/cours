import pandas as pd
from sklearn.model_selection import train_test_split
social = r"E:\cours_simplon\data_scientist\Machine_learning\arbres_de_decision\exo_social_network\Social_Network_Ads.csv"
df = pd.read_csv(social, sep= ",")
y=df['Purchased']
X=df.drop(['Purchased', 'Gender','User ID'],1)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state=0)
from sklearn.svm import SVC # "Support vector classifier"
svc = SVC(kernel='linear')
svc.fit(X, y)