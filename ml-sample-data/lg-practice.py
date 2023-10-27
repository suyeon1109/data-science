from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("ml-sample-data/Car details v3.csv")
unrelevent = ['name', 'torque', 'mileage','engine','max_power','fuel','owner','transmission','seller_type','max_power']
df = df.drop(columns=unrelevent)
df = df.dropna(axis=0)

# df['mileage'] = df.mileage.str.split(' ').str[0]
# df['mileage (kmpl)'] = df['mileage'].apply(pd.to_numeric)

# df['engine'] = df.engine.str.split(' ').str[0]
# df['engine (cc)'] = df['engine'].apply(pd.to_numeric)

# df['max_power'] = df.max_power.str.split(' ').str[0]
# df['max_power (bhp)'] = df['max_power'].apply(pd.to_numeric)

df.info()
print(df.head(10))

x = df[['year', 'km_driven', 'seats']]
y = df[['selling_price']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

model = LinearRegression()
model.fit(x_train.values, y_train.values)

predict_data = [[2014, 154000, 4]]
predicted = model.predict(predict_data)
print(predicted)

y_predict = model.predict(x_test.values)

plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel("Actual price")
plt.ylabel("Predicted price")
plt.title("MULTIPLE LINEAR REGRESSION")
plt.show()

plt.scatter(df[['X1 year']], df[['selling_price']], alpha=0.4)
plt.scatter(df[['X2 km_driven']], df[['selling_price']], alpha=0.4)
plt.scatter(df[['X3 fuel']], df[['selling_price']], alpha=0.4)
plt.scatter(df[['X4 seller_type']], df[['selling_price']], alpha=0.4)
plt.scatter(df[['X5 transmission']], df[['selling_price']], alpha=0.4)
plt.scatter(df[['X6 mileage']], df[['selling_price']], alpha=0.4)
plt.scatter(df[['X7 engine']], df[['selling_price']], alpha=0.4)
plt.scatter(df[['X8 max_power']], df[['selling_price']], alpha=0.4)
plt.scatter(df[['X9 torque']], df[['selling_price']], alpha=0.4)
plt.scatter(df[['X10 seats']], df[['selling_price']], alpha=0.4)
plt.show()

print(model.score(x_train.values, y_train.values))