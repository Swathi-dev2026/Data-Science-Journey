
### step 1:  Inheritance

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Student(Person):

    def __init__(self, name, course):         ### step 2: Adding student_specific data
        super().__init__(name)
        self.course = course

    def display_course(self):
        print(f"I am Studying {self.course}")

student1 = Student("Swathi" , "Data Science")

student1.introduce()
student1.display_course()
print("="*50)

### method overriding

class Person:

    def introduce(self):
        print("I am a person.")

class Student(Person):

    def introduce(self):
        print("I am a student.")

person1 = Person()
student1 = Student()

person1.introduce()
student1.introduce()

### Encapsulation

class Student:

