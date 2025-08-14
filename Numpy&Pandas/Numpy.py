#HANDS ON ASSIGNMENT
import numpy as np
# Q1. Create two-dimensional 3×3 array and perform ndim, shape, slicing operation on it.
arr_2d = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

print("Array:\n", arr_2d)
print("Number of dimensions (ndim):", arr_2d.ndim)
print("Shape:", arr_2d.shape)

print("Sliced Array (first 2 rows, first 2 cols):\n", arr_2d[:2, :2])


# Q2. Create one-dimensional array and perform ndim, shape, reshape operation on it.
arr_1d = np.array([10, 20, 30, 40, 50, 60])

print("Array:", arr_1d)
print("Number of dimensions (ndim):", arr_1d.ndim)
print("Shape:", arr_1d.shape)

reshaped_arr = arr_1d.reshape(2, 3)
print("Reshaped Array (2x3):\n", reshaped_arr)
