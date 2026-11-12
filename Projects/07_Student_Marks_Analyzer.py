
import numpy as np

marks = np.array([
    [78, 85, 92],
    [65, 70, 68],
    [90, 88, 95],
    [55, 60, 58],
    [82, 79, 85]
])

student_names = np.array([
    "Student 1",
    "Student 2",
    "Student 3",
    "Student 4",
    "Student 5"
])

print("Marks:")
print(marks)
print(student_names)

print("Shape:", marks.shape)
print("Total elements:", marks.size)

student_totals = marks.sum(axis = 1)
print("Student totals:", student_totals)

highest_index = student_totals.argmax()

print("Highest total index:", highest_index)

student_averages = marks.mean(axis=1)
print("Student averages:", student_averages)

high_scorers = student_averages >= 75
print("High scorer mask:", high_scorers)

high_scorer_averages = student_averages[student_averages >= 75]
print("High scorer averages:", high_scorer_averages)

high_scorer_marks = marks[student_averages >= 75]
print("High scorer marks:")
print(high_scorer_marks)

subject_averages = marks.mean(axis=0)
print("Subject averages:", subject_averages)

highest_subject_average = subject_averages.max()
highest_subject_index = subject_averages.argmax()
print("Highest subject average:", highest_subject_average)
print("Highest subject index:", highest_subject_index)

class_average = marks.mean()
print("Overall class average:", class_average)

print("Overall class average:", round(class_average, 2))

pass_mask = student_averages >= 60
print("Pass/Fail mask:", pass_mask)

pass_count = np.sum(pass_mask)
fail_count = len(student_averages) - pass_count
print("Students passed:", pass_count)
print("Students failed:", fail_count)