
import numpy as np

nums = np.array([1, 2, 3, 4, 5, 6])

print(nums.shape)

reshaped = nums.reshape(2,3)

print(reshaped)
print(reshaped.shape)
print("="*70)
### -1

#nums.reshape(2, -1)  # -1 means "unspecified", NumPy will calculate the appropriate size for that dimension

print(nums.reshape(2, -1))
print("="*70)
print(nums.reshape(-1, 2))  # -1 can also be used in the first dimension
print("="*70)
print(nums.reshape(-1, 3))  # -1 can also be used in the first dimension
print("="*70)
### flatten()
flattened = nums.flatten()
print(flattened)
print("="*70)
#ex

#marks.shape     # (2, 3)
#marks.flatten() # (6,)

### .T

marks = np.array([
    [80, 75, 90],
    [65, 88, 72]
])

print(marks.T)