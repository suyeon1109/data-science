import pandas as pd

# df1 = pd.DataFrame({'Key': ['A', 'B', 'C', 'D'],
#                     'Value1': [1, 2, 3, 4]})
# df2 = pd.DataFrame({'Key': ['B', 'D', 'E', 'F'],
#                     'Value2': [5, 6, 7, 8]})

# merged = df1.merge(df2, on='Key', how='outer')
# print(merged)

########################################################

# df1 = pd.DataFrame({'Key1': ['A', 'B', 'C', 'D'],
#                     'Key2': [1, 2, 3, 4],
#                     'Value1': [10, 20, 30, 40]})
# df2 = pd.DataFrame({'Key1': ['B', 'D', 'E', 'F'],
#                     'Key2': [2, 4, 5, 6],
#                     'Value2': [50, 60, 70, 80]})

# merged = df1.merge(df2, on=['Key1', 'Key2'])
# print(merged)


########################################################


# df1 = pd.DataFrame({'Key1': ['A', 'B', 'C', 'D'],
#                     'Value1': [10, 20, 30, 40]})
# df2 = pd.DataFrame({'Key2': ['B', 'D', 'E', 'F'],
#                     'Value2': [50, 60, 70, 80]})

# merged = df1.merge(df2, left_on='Key1', right_on='Key2')
# print(merged)


########################################################


# df1 = pd.DataFrame({'Value1': [10, 20, 30, 40]},
#                    index=['A', 'B', 'C', 'D'])
# df2 = pd.DataFrame({'Value2': [50, 60, 70, 80]},
#                    index=['B', 'D', 'E', 'F'])

# merged = df1.merge(df2, left_index=True, right_index=True)
# print(merged)


########################################################


df_sales = pd.DataFrame({'Product': ['A', 'B', 'C', 'D'],
                         'Sales': [100, 200, 150, 300]})

df_info = pd.DataFrame({'Product': ['B', 'D', 'E', 'F'],
                        'Category': ['Category1', 'Category2', 'Category1', 'Category2'],
                        'Price': [10.99, 19.99, 8.99, 15.99]})

# merged_inner = df_sales.merge(df_info, on='Product', how='inner')
# print("Inner join:")
# print(merged_inner)

# merged_left = df_sales.merge(df_info, on='Product', how='left')
# print("Left join:")
# print(merged_left)

# merged_right = df_sales.merge(df_info, on='Product', how='right')
# print("Right join:")
# print(merged_right)

# merged_outer = df_sales.merge(df_info, on='Product', how='outer')
# print("Outer join:")
# print(merged_outer)


########################################################


df_sales = pd.DataFrame({'Product': ['A', 'B', 'C', 'D'],
                         'Sales': [100, 200, 150, 300],
                         'Region': ['West', 'East', 'North', 'South']})

df_info = pd.DataFrame({'Product': ['B', 'D', 'E', 'F'],
                        'Category': ['Category1', 'Category2', 'Category1', 'Category2'],
                        'Price': [10.99, 19.99, 8.99, 15.99]})

df_customers = pd.DataFrame({'Product_Code': ['A', 'B', 'C', 'D', 'E'],
                             'Customer': ['John', 'Emma', 'Mike', 'Sophia', 'Oliver']})

df_region = pd.DataFrame({'Product_Code': ['B', 'D', 'E', 'F', 'G'],
                          'Region': ['West', 'East', 'North', 'South', 'Central'],
                          'Sales': [50, 100, 80, 70, 120]})

# merged_inner = df_sales.merge(df_info, on='Product', how='inner')
# print(merged_inner)
# print()

# merged_left_on = df_sales.merge(df_customers, left_on='Product', right_on='Product_Code', how='left')
# print(merged_left_on)
# print()

# merged_right_on = df_sales.merge(df_region, left_on='Product', right_on='Product_Code', how='right')
# print(merged_right_on)
# print()

df_sales.set_index('Product', inplace=True)
df_info.set_index('Product', inplace=True)
merged_inner_index = df_sales.merge(df_info, left_index=True, right_index=True, how='inner')
print(merged_inner_index)
print()