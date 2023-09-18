import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

url = "/Users/mac/Downloads/data.csv"

# Read dataset to pandas dataframe
dataset = pd.read_csv(url)
dataset.drop(columns=['id', 'Unnamed: 32'], inplace=True)
print(dataset.head(4))

x = dataset.iloc[:, 1:]
y = dataset.iloc[:, 0]

print(x.head(4))
print()
print(y.head(4))

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2)

# Data scaling
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)

# Evaluating the Algorithm
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(accuracy_score(y_test, y_pred))


# test various k values
scores = []
for i in range(1,16):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train,y_train)
    y_pred = knn.predict(x_test)
    scores.append(accuracy_score(y_test, y_pred))

# visualize the comparison
plt.plot(range(1,16),scores)
plt.show()