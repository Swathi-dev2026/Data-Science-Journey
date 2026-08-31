
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
print("="*70)
### Practical example: Logging
def log_function(func):
    def wrapper():
        print("Function is Starting...")
        func()
        print("Function has finished.")

    return wrapper

@log_function
def calculate():
    print("Calculating...")

calculate()