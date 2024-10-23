import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import decomposition
import seaborn as sns


df = pd.read_csv("iris.csv")
print(df.head(10))
array = df.values
X = array[:,0:4]
y = array[:,4]

kfold = KFold(n_splits=10)
model = KNeighborsClassifier(n_neighbors=3)
score = cross_val_score(model,X,y,cv=10)
print('\n\n')
print("Cross score before applying PCA\n")
print(score.mean())

print("Apply PCA now...")

pca = decomposition.PCA(n_components=1)
X_pca = pca.fit_transform(X)
core = cross_val_score(model,X_pca,y,cv=10)
print('\n\n')
print("Cross score After applying PCA\n")
print(score.mean())
