### Pandas: concatenation, merge, join

import pandas as pd
import numpy as np

### Concatenation
# data1 = pd.DataFrame(np.array([[0,1,2,3],[4,5,6,7]]), columns=['a','b','c','d'])
# data2 = pd.DataFrame(np.array([[8,9,10,11],[12,13,14,15]]), columns=['a','b','c','d'])

# print(data1)
# print(data2)

# # concat = pd.concat([data1,data2])
# concat = pd.concat([data1,data2], axis=1)
# print(concat)


# # Concatenate with original index values
# data1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# data2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
# print(data1)
# print(data2)

# concatenated_original_index = pd.concat([data1, data2], ignore_index=False)
# print("Concatenated with original index:")
# print(concatenated_original_index)
# print()

# # Concatenate with reset index
# concatenated_reset_index = pd.concat([data1, data2], ignore_index=True)
# print("Concatenated with reset index:")
# print(concatenated_reset_index)


# data1 = pd.DataFrame({
#    'id':[1,2,3,4,5],
#    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#    'subject_id':['sub1','sub2','sub4','sub6','sub5']})

# data2 = pd.DataFrame(
#    {'id':[1,2,3,4,5],
#    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#    'subject_id':['sub2','sub4','sub3','sub6','sub5']})

# print(data1)
# print()
# print(data2)
# print()

# concat = pd.concat([data1,data2])
# print(concat)




### Merge
# data1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# data2 = pd.DataFrame({'A': [1, 3, 4], 'C': [7, 8, 9]})

# print(data1)
# print()
# print(data2)
# print()

# # Inner merge
# merged_inner = pd.merge(data1, data2, how='inner')
# print("Inner merge:")
# print(merged_inner)
# print()

# # Outer merge
# merged_outer = pd.merge(data1, data2, how='outer')
# print("Outer merge:")
# print(merged_outer)
# print()

# # Left merge
# merged_left = pd.merge(data1, data2, how='left')
# print("Left merge:")
# print(merged_left)
# print()

# # Right merge
# merged_right = pd.merge(data1, data2, how='right')
# print("Right merge:")
# print(merged_right)

# Merge on 'A'
# merged_on = pd.merge(data1, data2, on='A', how='right')
# print(merged_on)
# print()

# # Merge on 'Key' and 'ID'
# data1 = pd.DataFrame({'Key': ['A', 'B', 'C', 'D', 'E'], 'Value': [1, 2, 3, 4, 5]})
# data2 = pd.DataFrame({'ID': ['A', 'B', 'D', 'E', 'F'], 'Score': [1, 2, 10, 20, 30]})

# print(data1)
# print()
# print(data2)
# print()

# merged_key = pd.merge(data1, data2, left_on='Value', right_on='Score')
# print(merged_key)

# # Merge on index
# data1 = pd.DataFrame({'Value': [1, 2, 3]}, index=['A', 'B', 'C'])
# data2 = pd.DataFrame({'Score': [10, 20, 30]}, index=['A', 'B', 'D'])

# print(data1)
# print()
# print(data2)
# print()

# merged_index = pd.merge(data1, data2, left_index=True, right_index=True, how='right')
# print(merged_index)


data1 = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})

data2 = pd.DataFrame(
   {'id':[3,4,5,6,7],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})

merged = pd.merge(data1, data2, on="id", how="left")
print(merged)