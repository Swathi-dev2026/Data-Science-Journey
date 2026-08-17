
import calculator

result1 = calculator.add(10, 5)
result2 = calculator.subtract(10, 5)

print(result1)
print(result2)
print("="*50)

### from.....import.....
from calculator import add, subtract

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
