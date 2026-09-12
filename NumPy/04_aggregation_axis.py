
import numpy as np

marks = np.array([10, 20, 30, 40, 50])

print("Sum:", marks.sum())
print("Mean:", marks.mean())
print("Minimum:", marks.min())
print("Maximum:", marks.max())
print("Standard Deviation:", marks.std())
print("="*70)

### 2D array

marks = np.array([
    [70, 80, 90],
    [65, 88, 72],                                   
    [70, 60, 85]
])

print("Column sums:", marks.sum(axis=0))
print("Row sums:", marks.sum(axis=1))
# axis=0 → calculation down the columns
# axis=1 → calculation across each row

print("Subject averages:", marks.mean(axis=0))
print("Student averages:", marks.mean(axis=1))

print(marks.max(axis=0))
print(marks.max(axis=1))

print(marks.std(axis=0))
print(marks.std(axis=1))