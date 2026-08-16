class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def introduce(self):
        print(f"Hello, Iam {self.name}.")

    def display_basic_info(self):
        print(f"Name  : {self.name}")
        print(f"Age  : {self.__age}")

class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student_info(self):
        print("===================================")
        self.display_basic_info()
        print(f"Course : {self.course}")
        print("===================================")

student1 = Student("Swathi", 22, "Data Science")
student2 = Student("Akash", 21, "Machine Learning")

student1.display_student_info()
student1.introduce()

student2.display_student_info()
student2.introduce()

