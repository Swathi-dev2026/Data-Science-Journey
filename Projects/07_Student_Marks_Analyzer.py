
import numpy as np

marks = np.array([
    [78, 85, 92],
    [65, 70, 68],
    [90, 88, 95],
    [55, 60, 58],
    [82, 79, 85]
])

print("Marks:")
print(marks)

print("Shape:", marks.shape)
print("Total elements:", marks.size)

student_totals = marks.sum(axis = 1)
print("Student totals:", student_totals)

highest_index = student_totals.argmax()

print("Highest total index:", highest_index)

student_averages = marks.mean(axis=1)
print("Student averages:", student_averages)

