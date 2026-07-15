
student = {"name" : "swathi",
           "age" : 22,
           "course" : "applied data science"}
print(student)
print(student["name"])
print(student["age"])
print(student["course"])

student["age"] = 23
print(student)

student["city"] = "chennai"
print(student)

student.pop("age")
print(student)

for key, value in student.items():
    print(key, ":" ,value)
