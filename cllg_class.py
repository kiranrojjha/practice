
import numpy as np
# arr_1d = np.array([1,2,3,4])
# arr_2d = np.array([[1,2,3],[4,5,6]])
# print(arr_1d)
# print(arr_2d)

# arr = np.array([[1,2,3],[4,5,6]])
# print("Dimensions:", arr.ndim)
# print("Shape(rowa,cols):", arr.shape)
# print("Total elemnts:", arr.size)
# print("Data type:", arr.dtype)

# a = np.array([1,2,3])
# b = np.array([5,6,7])
arr = np.arange(9).reshape(3, 3) 
first, second = np.split(arr, [1])  # Split after 1st row
print('first')
print('second')