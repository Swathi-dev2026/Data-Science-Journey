
#class Student:
 #   pass

#student1 = Student()

#print(student1)

### Adding data to a class

#class Student:

 #   def __init__(self, name, age):
  #      self.name = name
   #     self.age = age

#student1 = Student("Swathi", 22)

#print(student1.name)
#print(student1.age)

### Methods

#class Student:

 #   def __init__(self, name, age):
  #      self.name = name
   #     self.age = age

    #def display(self):
     #   print(f"Name: {self.name}")
      #  print(f"Age: {self.age}")

#student1 = Student("Swathi", 22)

#student1.display()

### calling methods on multiple objects

#class Student:

 #   def __init__(self, name, age):
  #      self.name = name
   #     self.age = age

    #def display(self):
     #   print(f"Name: {self.name}")
      #  print(f"Age : {self.age}")
       # print("--------------------")

#student1 = Student("Swathi", 22)
#student2 = Student("Rahul", 21)
#student3 = Student("Anjali", 23)

#student1.display()
#student2.display()
#student3.display()

### Adding another methon

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f" Name : {self.name}")
        print(f" Age : {self.age}")

    def greet(self):
        print(f"Hello, {self.name}! Welcome to python.")

student1 = Student("Swathi", 22)

student1.display()
student1.greet()