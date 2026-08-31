
### *args
def total(*args):
    print(args)
    print(sum(args))

total(10, 20, 30, 40)
print("="*70)

### *kwargs
def student_info(**kwargs):
    print(kwargs)

student_info(name="Swathi", age=22, course="Data Science")
print("="*70)

### Practice 1
def calculator_sum(*nums):
    print(sum(nums))

calculator_sum(10, 20, 30)
calculator_sum(5, 15, 25, 35)
print("="*70)

### Practice 2
def student(name, *marks, **details):
    print(name)
    print(marks)
    print(details)

student(
    "Swathi",
    90,98,99,
    course= "Data Science",
    semester = 3
)
print("="*70)

### Practice 3
def example(*args, **kwargs):
    print(args)
    print(kwargs)

example(10, 20, name="Swathi", course="Data Science")