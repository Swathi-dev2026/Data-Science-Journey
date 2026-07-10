
students = []
def add_student(students):
    student_name = input("Enter student Name: ")
    students.append(student_name)
    print("Student added scccessfully!")
add_student(students)
add_student(students)
add_student(students)
print(students)

def view_students(students):
    if len(students) == 0:
        print("No Students found.")
    else:
        print("Students:")

        for student in students:
            print(student)
view_students(students)

    
