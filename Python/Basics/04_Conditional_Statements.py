
#Practice 1

age = 20
if age>= 18:
    print("Adult")
else:
    print("Minor")

#Practice 2

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")

#Practice 3

x = 10
if x > 5 and x < 20:
    print("Inside")
else:
    print("Outside")

#Mission Chanllenge

name = input("Enter your name: ")
age = int(input("Enter your age: "))
password = input("Enter password: ")

if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

if age >= 18 and password == "python012":
    print(f"Hello, {name}!" + "You are eligible to vote.")
else:
    print(f"Sorry, {name}!" +"You are not eligible to vote.")

