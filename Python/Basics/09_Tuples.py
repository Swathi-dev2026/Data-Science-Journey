
student = ("Swathi", 22, "Data Science")
print(student)

print(student[0])
print(student[1])
print(student[2])
print("="*50)

#challenge 1

my_info = ("Swathi", 22, "Data science", "chennai", "SRM college")
print(my_info)
print(my_info[0])
print(my_info[4])
print("="*50)

#challenge 2

my_info = ("Swathi", 22, "Data science", "chennai", "SRM college")
print(len(my_info))
print(my_info[1:4])
print(my_info[:3])
print(my_info[2:])
print(my_info[-1])
print("="*50)

# Tuple Method 1:

nums = (10,20,10,30,10,40)
print(nums.count(10))                                    #Conut()

print(nums.index(30))                                    #Index()
print("="*50)

# Tuple loop

my_info = ("Swathi", 22, "Data science", "chennai", "SRM college")

for item in my_info:
    print(item)
print("="*50)

# Tuple + if

my_info = ("Swathi", 22, "Data science", "chennai", "SRM college")

for item in my_info:
    if item == "Data science":
        print("I am learning Data Scinece!")
print("="*50)

# Tuple -> List

my_info = ("Swathi", 22, "Data science", "chennai", "SRM college")
my_list = list(my_info)                                    #Tuple → List #list(tuple_name)
print(my_list)

# List -> Tuple
my_tuple = tuple(my_list)
print(my_tuple)
print("="*50)

#challenge 3

my_tuple = ("python", "SQL", "pandas")

my_list = list(my_tuple)

my_list.append("Numpy")                                   #append

my_tuple = tuple(my_list)

print(my_tuple)
print("="*50)

# challenge 4

colors = ("red", "blue", "green")

colors_list = list(colors)

colors_list.remove("blue")                                 #remove

colors = tuple(colors_list)

print(colors)