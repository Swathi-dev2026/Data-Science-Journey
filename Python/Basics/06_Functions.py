
def greet():
    print("Hello Swathi!")
greet()
print("=" *50)

# Function with parameters
def greet(name):
    print(f"Hello {name}!")
greet("Swathi")
greet("Akash")
greet("Sankar")
greet("Viji")
print("=" *50)

# Multi-parameter function
def add(a, b):
    print(a + b)
add(5, 10)
print("=" *50)

# Returning values
def add(a, b):
    return a + b
result = add(5, 8)
print("Returning value: ",result)

print("Example:-")
def square():
    return num * num
num = int(input("Enter a number: "))
result = square()
print(f"The Square value of {num} is {result}")
print("=" *50)

# Practice
def even( number):
    if number % 2 ==0:
        return True
    else:
        return False
print(even(9))
print("=" *50)

# Mission Challenge
def calculate_area(length, width):
    return length * width
area = calculate_area(10, 5)
print(area)
print("=" *50)

# Bonus challenge
def largest (a, b):
    if a > b:
        return a
    else:
        return b
print(largest(12,3))
