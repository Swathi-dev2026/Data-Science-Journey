
import numpy as np

marks = np.array([45, 60, 72, 80, 91])

print(marks > 70)
print(marks[marks > 70])  # boolean filtering
print("="*70)

### ex
marks = np.array([55, 68, 74, 81, 93])

print(marks >= 75)
print(marks[marks >= 75])
print("="*70)

### ex 2
marks = np.array([45, 60, 65, 72, 80, 85, 91])

print(marks[(marks >= 60) & (marks <= 80)])
print("="*70)

### ex 3
marks = np.array([45, 55, 65, 75, 85, 95])

print(marks[(marks < 60) | (marks > 80)])