
students = []
def add_student(students):
    student_name = input("Enter student Name: ")
    students.append(student_name)
    print("Student added scccessfully!")
#add_student(students)
#add_student(students)
#add_student(students)
#print(students)

def view_students(students):
    if len(students) == 0:
        print("No Students found.")
    else:
        print("Students:")

        for student in students:
            print(student)
#view_students(students)

def remove_student(students):
    student_name = input("Enter student name to remove: ")
    if student_name in students:
        students.remove(student_name)
        print("Student remove successfully")
    else:
        print("Student not found")
#remove_student(students)
#view_students(students)

def search_student(students):
    student_name = input("Enter student name to search: ")
    if student_name in students:
        print("Student found.")
    else:
        print("Student not found")
#search_student(students)
#view_students(students)

def count_student(students):
    print(f"Total Student: {len(students)}")
#count_student(students)

choice = 0
while choice != 6:
     print("================================")
     print("   STUDENT ATTENDANCE MANAGER   ")
     print("================================")
     print("1. Add Student")
     print("2. View Students")
     print("3. Remove Student")
     print("4. Search Student")
     print("5. Count Students")
     print("6. Exit")

     choice = int(input("Enter your choice: "))
     if choice == 1:
         add_student(students)
     elif choice == 2:
         view_students(students)
     elif choice == 3:
         remove_student(students)
     elif choice == 4:
         search_student(students)
     elif choice == 5:
         count_student(students)
     elif choice == 6:
         print("Thank you for using Student Attendance Manager!")
     else:
         print("Invalid choices. Please try again.")
    