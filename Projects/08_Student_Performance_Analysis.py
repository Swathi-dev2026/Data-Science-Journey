
import numpy as np
import csv
import os

# 1. Define subjects
subject_names = np.array(["Maths", "Science", "English"])

# 2. Get number of students
while True:
    try:
        num_students = int(input("Enter number of students: "))

        if num_students > 0:
            break
        else:
            print("Enter at least one student.")

    except ValueError:
        print("Please enter a valid number.")

# 3. Create empty lists
student_names = []
marks_data = []

# 4. Collect student information
for i in range(num_students):

    print(f"\nStudent {i + 1}")

    name = input("Enter student name: ").strip()
    student_names.append(name)

    student_marks = []

    for subject in subject_names:

        while True:
            try:
                score = int(input(f"Enter {subject} marks: "))

                if 0 <= score <= 100:
                    student_marks.append(score)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    marks_data.append(student_marks)

# 5. Convert lists into NumPy arrays
student_names = np.array(student_names)
marks = np.array(marks_data)

# 6. Display dataset
print("\n========== STUDENT DATA ==========")
print("Student Names:", student_names)
print("\nStudent Marks:")
print(marks)
print("\nArray Shape:", marks.shape)


# 7. Student Performance Analysis

student_totals = marks.sum(axis=1)
student_averages = marks.mean(axis=1)

print("\n========== STUDENT PERFORMANCE ==========")

for i in range(len(student_names)):

    result = "PASS" if student_averages[i] >= 60 else "FAIL"

    print(
        student_names[i],
        "| Total:", student_totals[i],
        "| Average:", round(student_averages[i], 2),
        "| Result:", result
    )

# 8. Find topper

topper_index = student_totals.argmax()

print("\nTopper:", student_names[topper_index])
print("Highest Total:", student_totals[topper_index])

# 9. Class statistics

print("\n========== CLASS STATISTICS ==========")
print("Class Average:", round(marks.mean(), 2))
print("Highest Mark:", marks.max())
print("Lowest Mark:", marks.min())

# 10. Student Rankings

ranking = np.argsort(student_totals)[::-1]

print("\n========== STUDENT RANKINGS ==========")

for position in range(len(ranking)):

    index = ranking[position]

    print(
        position + 1,
        student_names[index],
        "| Total:", student_totals[index]
    )


# 11. Grade Classification

grades = []

print("\n========== STUDENT GRADE REPORT ==========")

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

    grades.append(grade)

    print(
        student_names[i],
        "| Average:", round(average, 2),
        "| Grade:", grade
    )

grades = np.array(grades)

# 12. Grade Distribution

print("\n========== GRADE DISTRIBUTION ==========")

for grade in ["A+", "A", "B", "C", "F"]:

    count = np.sum(grades == grade)

    print(grade, ":", count, "student(s)")


# 13. Subject-wise Analysis

subject_averages = marks.mean(axis=0)

print("\n========== SUBJECT PERFORMANCE ==========")

for i in range(len(subject_names)):

    print(
        subject_names[i],
        "| Average:", round(subject_averages[i], 2),
        "| Highest:", marks[:, i].max(),
        "| Lowest:", marks[:, i].min()
    )

best_subject_index = subject_averages.argmax()
weakest_subject_index = subject_averages.argmin()

print("\nBest Subject:", subject_names[best_subject_index])
print("Weakest Subject:", subject_names[weakest_subject_index])

# 14. Pass Percentage

pass_mask = student_averages >= 60

pass_count = np.sum(pass_mask)
fail_count = len(student_names) - pass_count

pass_percentage = (pass_count / len(student_names)) * 100
fail_percentage = (fail_count / len(student_names)) * 100

print("\n========== PASS/FAIL ANALYSIS ==========")
print("Students Passed:", pass_count)
print("Students Failed:", fail_count)
print("Pass Percentage:", round(pass_percentage, 2), "%")
print("Fail Percentage:", round(fail_percentage, 2), "%")

# 15. Save Student Records to CSV

file_exists = os.path.exists("student_records.csv")

with open("student_records.csv", "a", newline="") as file:

    writer = csv.writer(file)

    # Write headings only if the file is new
    if not file_exists:

        writer.writerow([
            "Student Name",
            "Maths",
            "Science",
            "English",
            "Total",
            "Average",
            "Grade"
        ])

    # Write student records
    for i in range(len(student_names)):

        writer.writerow([
            student_names[i],
            marks[i][0],
            marks[i][1],
            marks[i][2],
            student_totals[i],
            round(student_averages[i], 2),
            grades[i]
        ])

print("\nStudent records saved successfully!")

# 16. Display Only Student Names

print("\n========== STUDENT NAMES ==========")

with open("student_records.csv", "r", newline="") as file:

    reader = csv.reader(file)

    next(reader)  # Skip column headings

    for row in reader:
        print(row[0])

# 17. Display Science Marks

print("\n========== SCIENCE MARKS ==========")

with open("student_records.csv", "r", newline="") as file:

    reader = csv.reader(file)

    next(reader)  # Skip headings

    for row in reader:
        print(row[0], "| Science:", row[2])

# 18. Calculate Average Science Marks from CSV

science_marks = []

with open("student_records.csv", "r", newline="") as file:

    reader = csv.reader(file)

    next(reader)  # Skip headings

    for row in reader:

        science_score = int(row[2])

        science_marks.append(science_score)

science_average = sum(science_marks) / len(science_marks)

print("\n========== SCIENCE STATISTICS FROM CSV ==========")
print("Total Students:", len(science_marks))
print("Average Science Marks:", round(science_average, 2))
print("Highest Science Mark:", max(science_marks))
print("Lowest Science Mark:", min(science_marks))

# 19. Identify Students with Low Marks

print("\n========== LOW MARK ALERT ==========")

with open("student_records.csv", "r", newline="") as file:

    reader = csv.reader(file)

    next(reader)  # Skip headings

    for row in reader:

        name = row[0]

        maths = int(row[1])
        science = int(row[2])
        english = int(row[3])

        if maths < 35 or science < 35 or english < 35:

            print(
                name,
                "| Maths:", maths,
                "| Science:", science,
                "| English:", english
            )