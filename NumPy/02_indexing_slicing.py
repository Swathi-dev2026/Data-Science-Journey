
### 1D indexing and slicing

import numpy as np

nums = np.array([10, 20, 30, 40, 50])

print(nums)

print(nums[0])
print(nums[2])
print(nums[4])
print("="*70)

# negative indexing

print(nums[-1])
print(nums[-2])
print("="*70)

# slicing

print(nums[1:4])
print("="*70)


# Practice

print(nums[:3])
print(nums[2:])
print(nums[1:5:2])
print("="*70)
print(nums[::2])
print(nums[::-1])
print("="*70)

### 2D indexing and slicing

students = np.array([
    [10, 80, 75],
    [15, 90, 88],
    [8, 70, 65]
])

print(students)

# Access individual elements
print(students[0, 1])  # Accessing the element in the first row and second column
print(students[1, 2])  # Accessing the element in the second row and third column
print(students[2, 1])  # Accessing the element in the third row and second column
print("="*70)
print(students[0, 0])
print(students[1, 2])
print(students[2, 1])

# To select the entire row

print(students[0])
print(students[1])
print("="*70)

# To select the entire column

print(students[:, 0])
print(students[:, 1])
print(students[:, 2])
print("="*70)

# 2D slicing

print(students[0:2, 1:3])  # Slicing the first two rows and the last two columns
print("="*70)

# Practice

print(students[1:, :2])



