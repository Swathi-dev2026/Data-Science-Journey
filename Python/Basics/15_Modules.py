
import my_package.calculator

result1 = my_package.calculator.add(10, 5)
result2 = my_package.calculator.subtract(10, 5)

print(result1)
print(result2)
print("="*50)

### from.....import.....
from my_package.calculator import add, subtract

print(add(20, 10))
print(subtract(20, 10))
print("="*50)

### built-in modules(math)
import math

print(math.sqrt(25))     #Square root of 25
print(math.pow(2, 3))    #2 to the power of 3, basically cube
print(math.pi)           #the value of the pi
print("="*50)

### random Module
import random

num = random.randint(1, 10)    # random integer

print(num)
print("="*50)

### random.choice()
import random

fruits = ["apple", "orange", "grapes", "pineapple", "strawberry"]

selected_fruits = random.choice(fruits)   # random item

print(selected_fruits)
print("="*50)

### after creaiting a package, we can import the modules from the package and use them in our code. 

from my_package.greetings import greet

greet("Swathi")
print("="*50)

from my_package.calculator import add, subtract, multiply
from my_package.greetings import greet, welcome

print("Addition: ", add(10, 5))
print("Subtraction: ", subtract(10, 5))
print("Multiplication: ", multiply(10, 5))

greet("Swathi")
welcome("Swathi")

