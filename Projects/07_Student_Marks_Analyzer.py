
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
print("Overall class average:", round(class_average, 2))

pass_mask = student_averages >= 60
print("Pass/Fail mask:", pass_mask)

print("Topper:", student_names[highest_index])

pass_count = np.sum(pass_mask)
fail_count = len(student_averages) - pass_count
print("Students passed:", pass_count)
print("Students failed:", fail_count)

print("\nStudent Performance:")

for i in range(len(student_names)):
    result = "PASS" if student_averages[i] >= 60 else "FAIL"

    print(
        student_names[i],
        "| Total:", student_totals[i],
        "| Average:", round(student_averages[i], 2),
        "| Result:", result
    )
print("\nSubject Performance:")
subject_names = np.array([
    "Maths",
    "Science",
    "English"
])

print("Best performing subject:", subject_names[highest_subject_index])

ranking = np.argsort(student_totals)[::-1]

print("\nStudent Rankings:")

for position in range(len(ranking)):
    index = ranking[position]

    print(
        position + 1,
        student_names[index],
        "| Total:", student_totals[index]
    )

for i in range(len(student_names)):

    average = student_averages[i]

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "F"

    print(
        student_names[i],
        "| Average:", round(average, 2),
        "| Grade:", grade
    )

grades = []

for average in student_averages:

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "F"

    grades.append(grade)

grades = np.array(grades)

print("\nGrade Distribution:")

for grade in ["A+", "A", "B", "C", "F"]:
    count = np.sum(grades == grade)
    print(grade, ":", count, "student(s)")

lowest_index = student_totals.argmin()

print("\nLowest Performing Student:")
print("Name:", student_names[lowest_index])
print("Total:", student_totals[lowest_index])
print("Average:", round(student_averages[lowest_index], 2))

print("\nSubject Performance:")

for i in range(len(subject_names)):
    print(
        subject_names[i],
        "| Average:", round(subject_averages[i], 2)
    )

subject_highest = marks.max(axis=0)
subject_lowest = marks.min(axis=0)

print("\nSubject-wise Highest Marks:", subject_highest)
print("Subject-wise Lowest Marks:", subject_lowest)

print("\n========== CLASS SUMMARY ==========")

print("Total Students:", len(student_names))
print("Class Average:", round(marks.mean(), 2))
print("Highest Mark:", marks.max())
print("Lowest Mark:", marks.min())
print("Students Passed:", pass_count)
print("Students Failed:", fail_count)

print("Topper:", student_names[student_totals.argmax()])
print("Lowest Performer:", student_names[student_totals.argmin()])

print("Best Subject:", subject_names[subject_averages.argmax()])
print("Weakest Subject:", subject_names[subject_averages.argmin()])