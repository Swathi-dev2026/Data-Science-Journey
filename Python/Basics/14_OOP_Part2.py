
### Inheritance

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Student(Person):
    pass

student1 = Student("Swathi")

student1.introduce()
