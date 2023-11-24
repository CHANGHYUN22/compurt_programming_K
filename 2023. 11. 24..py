import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score



filename = "./data/09_irisdata.csv"

column_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']


data = pd.read_csv(filename, names = column_names)

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

model = DecisionTreeClassifier()

kfold = KFold(n_splits=10, random_state=5, shuffle=True)

results = cross_val_score(model, X, y, cv=kfold)

print(results.mean())
print(data.shape)
print(data.describe())

import matplotlib
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

data = pd.read_csv(filename, names = column_names)

scatter_matrix(data)
plt.savefig("./data/09_irisdata.png")



