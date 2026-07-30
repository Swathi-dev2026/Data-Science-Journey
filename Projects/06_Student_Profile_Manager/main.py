
student = {}

def add_student_profile(student):
    if len(student) != 0:
        print("Student profile already exists.")
        print("Please delete the existing profile before adding a new one.")
    else:
        student["name"] = input("Enter your name: ")
        student["roll_number"] = input("Enter your roll number: ")
        student["age"] = int(input("Enter your age: "))
        student["course"] = input("Enter your course: ")
        student["city"] = input("Enter your city: ")

        print("Student profile added successfully!")
#add_student_profile(student)
#print(student)

def view_student_profile(student):
    if len(student) == 0:
        print("No student profile found.")
    else:
        print("=========================================")
        print("STUDENT PROFILE                          ")
        print("=========================================")
        print(f"Name        : {student['name']}")
        print(f"Roll Number : {student['roll_number']}")
        print(f"Age         : {student['age']}")
        print(f"Course      : {student['course']}")
        print(f"City        : {student['city']}")
        print("=========================================")
#view_student_profile(student)

def update_student_profile(student):
    if len(student) == 0:
        print("No student profile found.")
    else:
        print("1. Update Name")
        print("2. Update Roll Number")
        print("3. Update Age")
        print("4. Update Course")
        print("5. Update City")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            student["name"] = input("Enter new name: ")
            print("Name updated successfully!")
        elif choice == 2:
            student["roll_number"] = input("Enter new roll number: ")
            print("Roll number updated successfully!")
        elif choice == 3:
            student["age"] = int(input("Enter updated Age: "))
            print("Age updated successfully!")
        elif choice == 4:
            student["course"] = input("Enter new course:")
            print("Course updated successfully!")
        elif choice == 5:
            student["city"] = input("Enter new city:")
            print("City updated successfully!")
        else:
            print("Invalid choice. Please try again.")

#update_student_profile(student)

def delete_student_profile(student):
    if len(student) == 0:
        print("No student profile found")
    else:
        student.clear()
        print("Student Profile deleted successfully!")
#delete_student_profile(student)
#print(student)

def search_student_profile(student):
    if len(student) == 0:
        print("No student profile found.")
    else:
        print("1. Search by Name")
        print("2. Search by Roll Number")
        print("3. Search by Course")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            search_name = input("Enter the name to search: ")
            if search_name == student["name"]:
                print("Student Found")
            else:
                print("Student not found")
        elif choice == 2:
            search_roll_number = input("Enter roll number to search: ")
            if search_roll_number == student["roll_number"]:
                print("Student Found")
            else:
                print("Student not found: ")
        elif choice == 3:
            search_course = input("Enter course to search: ")
            if search_course == student["course"]:
                print("Student found")
            else:
                print("Student not found")
        else:
            print("Invalid Choice. Please try again.")
            
choice = 0
while choice != 6:
    print("=============================================")
    print(" STUDENT PROFILE MANAGER ")
    print("=============================================")
    print("1. Add Student Profile")
    print("2. View Student Profile")
    print("3. Update Student Profile")
    print("4. Delete Student Profile")
    print("5. Search Student Profile")
    print("6. Exit")

    choice = int(input("Enter your Choice:"))

    if choice == 1:
        add_student_profile(student)
    elif choice == 2:
        view_student_profile(student)
    elif choice == 3:
        update_student_profile(student)
    elif choice == 4:
        delete_student_profile(student)
    elif choice == 5:
        search_student_profile(student)
    elif choice == 6:
        print("Thank you for using Student Profile Manager!")
    else:
        print("Invalid choice. Please try again.")
