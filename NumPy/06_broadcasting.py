
import numpy as np

marks = np.array([10, 20, 30, 40, 50])

print(marks + 5)  # add 5 to each element
print("="*70)

### 2 rows

marks = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

bonus = np.array([5, 10, 15])

print(marks + bonus)  # broadcasting adds bonus to each row of marks
print("="*70)

### challenge

marks = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

bonus =10

print(marks + bonus) 

print(marks * 2)  # multiply each element by 2
print("="*70)