

def get_student_details(): 
    name = input("Enter your name: ")
    roll_num = input("Enter your roll number: ")

    while True:
        marks = int(input("Enter your marks: "))

        if 0 <= marks <= 100:
            break
        print("Invalid Marks! Please enter marks between 0 and 100.")
    return name, roll_num, marks

    
def calculate_grade(marks):
    if marks > 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
                                   

def calculate_result(marks):
    if marks >= 60:
        return "PASS"
    else:
        return "FAIL"


def motivational_message(marks):
    if marks > 90:
        return "Outstanding Performance!"
    elif marks >= 80:
        return "Great Job!"
    elif marks >= 70:
        return "Good Work!"
    elif marks >= 60:
        return "Keep Practicing!"
    else:
        return "Better Luck Next Time!"


def display_report(name, roll_num, marks, grade, result, message):
    print("==============================================")
    print(            "STUDENT RESULT SYSTEM"             )
    print("==============================================")

    print("Name        : ",name)                        
    print("Roll Number : ",roll_num)
    print("Marks       : ",marks)
    print("Grade       : ",grade)
    print("Result      : ",result)

    print (message)

    print("==============================================")


choice = "yes"

while choice == "yes":

    name, roll_num, marks = get_student_details()

    grade = calculate_grade(marks)

    result = calculate_result(marks)

    message = motivational_message(marks)

    display_report(name, roll_num, marks, grade, result, message)

    choice = input("Do you want to evaluate another student? (yes/no): ").lower()

print("Thank you for using Student Result System!")
    





    


    
    