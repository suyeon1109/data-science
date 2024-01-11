 import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree  #시각화 툴

df = pd.read_csv('heart_v2.csv')
# print(df.head())
# sns.countplot(df['heart disease'])
# plt.title('Value counts of heart disease patients')
# plt.show()

X = df.drop('heart disease',axis=1)
y = df['heart disease']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42)

classifier_rf = RandomForestClassifier(random_state=42, n_jobs=-1, max_depth=5, n_estimators=100, oob_score=True)

classifier_rf.fit(X_train, y_train)

# print(classifier_rf.oob_score_)

plt.figure(figsize=(30,10))
plot_tree(classifier_rf.estimators_[5], feature_names=['age', 'sex', 'BP', 'cholestrol'], class_names=['Disease', "No Disease"],filled=True)
plt.show()

plt.figure(figsize=(30,10))
plot_tree(classifier_rf.estimators_[7], feature_names=['age', 'sex', 'BP', 'cholestrol'], class_names=['Disease', "No Disease"],filled=True)
plt.show()

plt.figure(figsize=(30,10))
plot_tree(classifier_rf.estimators_[1], feature_names=['age', 'sex', 'BP', 'cholestrol'], class_names=['Disease', "No Disease"],filled=True)
plt.show()