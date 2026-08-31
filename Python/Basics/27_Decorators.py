
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