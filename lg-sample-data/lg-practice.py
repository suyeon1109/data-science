from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Car details v3.csv")
x = df[['year','km_driven','fuel','seller_type','transmission','mileage','engine','max_power','torque','seats']]
y = df[['selling_price']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

model = LinearRegression()
model.fit(x_train.values, y_train.values)

predict_data = [[2014.23, 20, 310, 4, 24.98654, 121.56998]]
predicted = model.predict(predict_data)
print(predicted)

y_predict = model.predict(x_test.values)

plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel("Actual price")
plt.ylabel("Predicted price")
plt.title("MULTIPLE LINEAR REGRESSION")
plt.show()

plt.scatter(df[['X1 transaction date']], df[['Y house price of unit area']], alpha=0.4)
plt.scatter(df[['X2 house age']], df[['Y house price of unit area']], alpha=0.4)
plt.scatter(df[['X3 distance to the nearest MRT station']], df[['Y house price of unit area']], alpha=0.4)
plt.show()

print(model.score(x_train.values, y_train.values))