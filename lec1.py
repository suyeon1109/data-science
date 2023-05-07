import numpy as np

# Creating array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# # What is dimension?
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# # Indexing
# print(b[1])
# print(c[0,1])
# print(d[0,1,2])

# # Slicing
# print(b[1:5])
# print(c[1, 1:4])

# # Data Type
# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr.dtype)

# # Shape
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr.shape)

# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('shape of array :', arr.shape)

# # Reshape
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)
# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 3, 2)
# print(newarr)

# # Flattening
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(-1)
# print(newarr)

# # Transpose
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.T
# newarr = arr.transpose()
# print(newarr)

# # 2D iteration
# arr = np.array([[1, 2, 3], [4, 5, 6]])

# for x in arr:
#   for y in x:
#     print(y)

# # nd iteration
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr):
#    print(x)

# # Concatenation
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2))
# print(arr)

# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=0)
# print(arr)

# # Search
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4)
# print(x)

# # Sorting
# arr = np.array([3, 2, 0, 1])
# print(np.sort(arr))

# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))

# # Broadcasting
# A = np.arange(32).reshape(4, 1, 8)
# B = np.arange(48).reshape(1, 6, 8)
# print(A+B)