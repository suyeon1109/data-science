from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

passengers = pd.read_csv("passengers.csv")
# print(passengers.shape)
# print(passengers.head())

passengers['Sex'] = passengers['Sex'].map({'female': 1, 'male': 0})     # 다른 value로 변환시켜주는 함수 map
passengers['Age'].fillna(value=passengers['Age'].mean(), inplace=True)
passengers['FirstClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 1 else 0)
passengers['SecondClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 2 else 0)

features = passengers[['Sex', 'Age', 'FirstClass', 'SecondClass']]
survival = passengers['Survived']

print(features.head())

train_features, test_features, train_labels, test_labels = train_test_split(features, survival)

scaler = StandardScaler()
train_features = scaler.fit_transform(train_features)
test_features = scaler.transform(test_features)

model = LogisticRegression()
model.fit(train_features, train_labels)

# print(model.score(train_features, train_labels))

# print(model.score(test_features, test_labels))

# print(model.coef_)