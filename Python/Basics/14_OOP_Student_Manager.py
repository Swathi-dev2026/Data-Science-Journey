
class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.__age = age
        self.course = course

    def display(self):
        print("===================================")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.__age}")
        print(f"Course : {self.course}")
        print("===================================")

    def introduce(self):
        print(f"Hello, I am {self.name}.")

student1 = Student("Swathi", 22, "Data Science")
student2 = Student("Akash", 21, "Machine Learning")

student1.display()
student1.introduce()

student2.display()
student2.introduce()

