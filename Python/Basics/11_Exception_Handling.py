
try:
    age = int(input("Enter your age: "))
    print(f"Your age is {age}")
except:
    print("Please enter a valid number.")
print("="*50)

# Specific Errors

try:
    age = int(input("Enter your age: "))
    print(f"Your age is {age}")
except ValueError:
    print("Please enter a valid number.")
print("="*50)

# different types of errors

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")
print("="*50)

# else block

try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print(f"Result: {result}")
print("="*50)


#finally block

try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print(f"Result: {result}")

finally:
    print("Execution completed.")
