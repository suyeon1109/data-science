import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# random integer
# x = np.random.randint(100)
# print(x)

# # random array
# arr = np.random.randint(100, size=(5))
# arr = np.random.randint(100, size=(3, 5))
# print(arr)

# random distribution
# arr = np.random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
# print(arr)

# normal distribution
# x = np.random.normal(size=(2, 3))
# print(x)

# matplotlib pyplot
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

# # matplotlib markers
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker='o')
# # plt.plot(ypoints, marker = '*')
# # plt.plot(ypoints, linestyle = 'dotted')
# # plt.plot(ypoints, linestyle = 'dashed')
# plt.show()

# # labeling
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y)

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.show()

# # Scatter plot
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# plt.scatter(x, y)
# plt.show()

# #day one, the age and speed of 13 cars:
# x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
# y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
# plt.scatter(x, y)

# #day two, the age and speed of 15 cars:
# x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
# y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])
# plt.scatter(x, y)

# plt.show()

# # Bar graphs
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x, y)
# # plt.barh(x, y)
# # plt.bar(x, y, color = "red")
# # plt.bar(x, y, width = 0.1)
# plt.show()




# Practical Example
# cols = ['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'IsActiveMember', 'EstimatedSalary', 'Exited']
# churn = pd.read_csv("C:/Users/ZCL/Downloads/archive/Churn_Modelling.csv", usecols=cols)
# print(churn.head)

# plt.figure(figsize=(8,5))
# plt.title("Number of Customers", fontsize=14)
# plt.bar(x=churn['Geography'].value_counts().index, height=churn.Geography.value_counts().values)
# plt.show()

# plt.hist(x=churn['Balance'])
# plt.show()

# sample = churn.sample(n=200, random_state=42) #small sample
# plt.scatter(x=sample['CreditScore'], y=sample['Age'])

# plt.title("Credit Score vs Age", fontsize=15)
# plt.hist2d(x=churn.CreditScore, y=churn.Age)