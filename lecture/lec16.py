from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### univariate linear regression

# df = pd.read_csv("weight-height.csv")
# print(df.head())

# x = df["Height"]
# y = df["Weight"]
# plt.plot(x, y, 'o')
# plt.show()

# model = LinearRegression()
# model.fit(x.values.reshape(-1,1), y)

# predicted = model.predict(x.values.reshape(-1,1))

# print(model.predict([[70]]))
# print(model.coef_)
# print(model.intercept_)
# plt.plot(x, predicted)  
# plt.show()

# print(model.score(x.values.reshape(-1,1), y))   # R squared (maximum value = 1), 1에 가까울수록 정확도가 높은 모델이다




### multivariate linear regression

# df = pd.read_csv("Real estate.csv")
# x = df[['X1 transaction date', 'X2 house age', 'X3 distance to the nearest MRT station', 'X4 number of convenience stores', 'X5 latitude', 'X6 longitude']]
# y = df[['Y house price of unit area']]

# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

# model = LinearRegression()
# model.fit(x_train.values, y_train.values)

# predict_data = [[2014.23, 20, 310, 4, 24.98654, 121.56998]]
# predicted = model.predict(predict_data)
# print(predicted)

# y_predict = model.predict(x_test.values)

# plt.scatter(y_test, y_predict, alpha=0.4)
# plt.xlabel("Actual price")
# plt.ylabel("Predicted price")
# plt.title("MULTIPLE LINEAR REGRESSION")
# plt.show()

# plt.scatter(df[['X1 transaction date']], df[['Y house price of unit area']], alpha=0.4)
# plt.scatter(df[['X2 house age']], df[['Y house price of unit area']], alpha=0.4)
# plt.scatter(df[['X3 distance to the nearest MRT station']], df[['Y house price of unit area']], alpha=0.4)
# plt.show()

# print(model.score(x_train.values, y_train.values))