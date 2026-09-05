 
### 1. Creating a 1D array

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)
print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)
print("="*70)

## Practice

arr2 = np.array([5, 10, 15, 20, 25, 30])
print(arr2)
print("Dimensions:", arr2.ndim)
print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Data type:", arr2.dtype)
print("="*70)

### 2. Creating a 2D array

marks = np.array([
    [98,89,90],
    [87,98,97]
])

print(marks)

print("dimension:",marks.ndim)
print("Shape:", marks.shape)
print("Size:", marks.size)
print("="*70)

students = np.array([
    [10, 80, 75,],
    [15, 90, 88],
    [8, 70, 65]
])
print(students)
print("Dimensions:", students.ndim)
print("Shape:", students.shape)
print("Size:", students.size)