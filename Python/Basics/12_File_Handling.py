
### step 1: Writing data to a file

#file = open("student.txt","w")

#file.write("Name: Swathi\n")
#file.write("Course: Applied data science\n")
#file.write("College: SRM University\n")

#file.close()

#print("Data written successfully!")

### step 2: Reading data from a file

#file = open("student.txt","r")

#content = file.read()

#print(content)

#file.close()

### step 3: Appending data to a file

#file = open("student.txt","a")

#file.write("City: Chennai\n")

#file.close()

#print("Data appended successfully!")

### step 4: The professional way to handle files( with open )


with open("student.txt","r") as file:
    content = file.read()

    print(content)

print ("File closed automatically after the with block")