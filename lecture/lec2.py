import numpy as np
import cv2 as cv

# Create 4*4 array
# a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# print(a)

# Create 12*6*3 array
# b = np.array([])
# b.reshape(12,6,3)

# Create 3*3 array ranging from 2 to 10
# b = np.arange(2,11).reshape(3,3)
# print(b)

# Slice the array
# print(b[0,2])
# print(b[1,1])

# c = np.array([[[1,2],[3,4],[5,6]]])
# print(c)
# print(c[0,1,1])
# print(c[0,2,0])

# A = np.arange(32).reshape(4, 2, 4)
# print(A)
# print(A[1,1,1])


# Flatten the array
# newA=A.reshape(-1)
# print(newA)

# Search the element
# x = np.where(A==13)
# print(x)

# Join and sort two arrays
# a = np.array([0,10,50,40,80])
# b = np.array([20,60,30,90])
# arr = np.concatenate((a,b))
# print(arr)
# print(np.sort(arr))

# Reverse the array
# arr = np.arange(9).reshape(3,3)
# arr=np.flip(arr)
# print(arr)

# Fill with zero
arr = np.zeros(10)
print(arr)


# Image manipulation
# img = cv.imread("C:/Users/ZCL/Pictures/Camera Roll/PCB Board.jpg")
# img = img*2
# print(img[0,0])
# cv.imshow("frame", img)
# cv.waitKey(0)