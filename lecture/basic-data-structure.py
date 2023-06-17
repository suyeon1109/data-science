import numpy as np

#array
arr = np.array([1,2,3])
print(arr)

#tuple
tpl = (4,5,6)
arr=np.array(tpl) # convert tuple to array
print(arr)

#list
list = [1,2,3]
arr = np. array(list) # convert list to array
print(arr)

# array != list
type([1,2,3]) # list
type(arr) # numpy.ndarray

# shape of array
arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr1.shape, arr2.shape) # (3.) (2.3)

#ndim (=dimension)
print(arr1.ndim,arr2.ndim) # 1 2

#size
print(arr1.size,arr2.size) # 3 6


# data type of array
arr = np.array([1,2,3], dtype=float) # X data type specification => detects data type
print(arr, arr.dtype) #[1. 2. 3.] float64 
# number after data type = bits used in memory to express each element of array)
arr = np.array([0,1,1], dtype=bool)
print(arr,arr.dtype) # [False True False] bool

# changing data type of an array
arr = np.array([0,1,2,3])
print(arr,arr.dtype) # [0 1 2 3] int64

arr = arr.astype(np.float32)
print(arr,arr.dtype) #[0. 1. 2. 3.] float32


# when an array contains more than one data type
arr = np.array([1,2,3.4,"64"])
print(arr,arr.dtype) # ["1" "2" "3.4" "64"] <U32 (=converted to unicode type)

arr = np.array([1,2,3.4,"64"], dtype=int)
print(arr,arr.dtype) # [1 2 3 64] int64

arr = np.array([1,2,3.4,"64 string"], dtype=int)
print(arr,arr.dtype) # valueError