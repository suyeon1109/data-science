import pandas as pd

# Pandas Basic Calculation

df = pd.DataFrame({'A': [1, 2, 3, 4],
                   'B': [5, 6, 7, 8]})

# column_sum = df['B'].sum()
# print("Column Sum:")
# print(column_sum)


# df['Row Sum'] = df.sum(axis=1)
# print("Row Sum:")
# print(df)


# column_mean = df['B'].mean()
# print("Column Mean:")
# print(column_mean)


# column_max = df['A'].max()
# column_min = df['B'].min()

# print("Column Maximum:")
# print(column_max)
# print("Column Minimum:")
# print(column_min)


# df['A Cumulative Sum'] = df['A'].cumsum()
# print("Cumulative Sum:")
# print(df)

# df['new column'] = df['A'] / df['B']
# print(df)


# Mapping

# x = pd.Series({'one':1,'two':2,'three':3})
# y = pd.Series({1:'triangle',2:'square',3:'circle'})

# x.map(y)

# y.map(x)