
import numpy as np
import csv
import os

# CSV file location
csv_file = os.path.join(
    os.path.dirname(__file__),
    "student_records_v2.csv"
)

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

student_ids = []
existing_student_ids = []

student_names = []
marks_data = []

# Load previously saved Student IDs

if os.path.exists(csv_file):

    with open(csv_file, "r", newline="") as file:

        reader = csv.reader(file)
        next(reader)

        for row in reader:
            existing_student_ids.append(row[0])
# 4. Collect student information
for i in range(num_students):

    print(f"\nStudent {i + 1}")

    # Collect unique student ID
    while True:

        student_id = input("Enter student ID: ").strip()

        if student_id == "":
            print("Student ID cannot be empty.")

        elif student_id in student_ids or student_id in existing_student_ids:
            print("This Student ID already exists. Enter another ID.")

        else:
            student_ids.append(student_id)
            break

    # Collect student name
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
        student_ids[i],
        "|", student_names[i],
        "| Total:", student_totals[i],
        "| Average:", round(student_averages[i], 2),
        "| Result:", result
    )

# 8. Find topper

topper_index = np.argmax(student_totals)

print("\nTopper:", student_ids[topper_index], "|", student_names[topper_index])
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
        student_ids[index],
        "|", student_names[index],
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
    student_ids[i],
    "|", student_names[i],
    "| Average:", round(student_averages[i], 2),
    "| Grade:", grades[i]
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

# 15. Save student records to CSV


file_exists = os.path.exists(csv_file)

with open(csv_file, "a", newline="") as file:

    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Student ID",
            "Student Name",
            "Maths",
            "Science",
            "English",
            "Total",
            "Average",
            "Grade"
        ])

    for i in range(len(student_names)):

        writer.writerow([
            student_ids[i],
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

with open(csv_file, "r", newline="") as file:

    reader = csv.reader(file)

    next(reader)  # Skip column headings

    for row in reader:
        print(row[1])  # Student names are in the 2nd column (index 1)

# 17. Display Science Marks

print("\n========== SCIENCE MARKS ==========")

with open(csv_file, "r", newline="") as file:

    reader = csv.reader(file)

    next(reader)  # Skip headings

    for row in reader:
        print(row[1], "| Science:", row[3])

# 18. Calculate Average Science Marks from CSV

science_marks = []

with open(csv_file, "r", newline="") as file:

    reader = csv.reader(file)

    next(reader)  # Skip headings

    for row in reader:

        science_score = int(row[3])  # Science marks are in the 4th column (index 3)

        science_marks.append(science_score)

science_average = sum(science_marks) / len(science_marks)

print("\n========== SCIENCE STATISTICS FROM CSV ==========")
print("Total Students:", len(science_marks))
print("Average Science Marks:", round(science_average, 2))
print("Highest Science Mark:", max(science_marks))
print("Lowest Science Mark:", min(science_marks))

# 19. Identify students with low marks

print("\n========== LOW MARK ALERT ==========")

with open(csv_file, "r", newline="") as file:

    reader = csv.reader(file)
    next(reader)

    for row in reader:

        student_name = row[1]
        student_id = row[0]

        maths = int(row[2])
        science = int(row[3])
        english = int(row[4])

        if maths < 35 or science < 35 or english < 35:
            print(f"{student_id} | {student_name} has scored below 35 in at least one subject.")


# 20. Search Student by ID or Name

print("\n========== STUDENT SEARCH ==========")
print("1. Search by Student ID")
print("2. Search by Student Name")

choice = input("Enter your choice (1 or 2): ").strip()

if choice == "1":
    search_value = input("Enter Student ID: ").strip()
    search_column = 0

elif choice == "2":
    search_value = input("Enter Student Name: ").strip()
    search_column = 1

else:
    search_value = ""
    search_column = None
    print("Invalid choice. Please select 1 or 2.")

if search_column is not None:

    if search_value == "":
        print("Search value cannot be empty.")

    else:
        found = False

        with open(csv_file, "r", newline="") as file:

            reader = csv.reader(file)
            next(reader)

            for row in reader:

                if row[search_column].lower() == search_value.lower():

                    print("\nStudent Found!")
                    print("Student ID:", row[0])
                    print("Student Name:", row[1])
                    print("Maths:", row[2])
                    print("Science:", row[3])
                    print("English:", row[4])
                    print("Total:", row[5])
                    print("Average:", row[6])
                    print("Grade:", row[7])

                    found = True
                    break

        if not found:
            print("Student record not found.")
