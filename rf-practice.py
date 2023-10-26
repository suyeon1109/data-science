# Data Processing
import pandas as pd
import numpy as np

# Modelling
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint

# Tree Visualisation
from sklearn.tree import export_graphviz
from IPython.display import Image
import graphviz

df = pd.read_csv("lg-sample-data/Car details v3.csv")
unrelevent = ['name','owner','transmission','seller_type','max_power', 'year', 'km_driven']
df = df.drop(columns=unrelevent)
df = df.dropna(axis=0)

df.info()
print(df.head(10))

x = df[['torque', 'mileage','engine','max_power','fuel','max_power','selling_price']]
y = df[['seats']]