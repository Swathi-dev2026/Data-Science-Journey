
student_name = input("Enter your name: ")
roll_number = input("Enter your roll number: ")
marks = int(input("Enter your marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks entered. Please enter marks between 0 and 100.")
    exit()

if marks >=90:
    grade = "A"
elif marks >=80:
    grade = "B"
elif marks >=70:
    grade = "C"
elif marks >=60:
    grade = "D"
else:
    grade = "F"



print("=====================================")
print(       "STUDENT REPORT CARD"           )
print("=====================================")

print("Name          : ", student_name)
print("Roll Number   : ", roll_number)
print("Marks         : ", marks)
print("Grade         : ", grade)
if marks >= 60:
    result = "PASS"
else:
    result = "FAIL"
print("Result        : ", result) 

if marks >= 60:
    print("Excellent Work!")
else:
    print("Better Luck Next Time!")

print("=====================================")