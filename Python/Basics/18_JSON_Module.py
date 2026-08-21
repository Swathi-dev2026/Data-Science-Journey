
### Step 1: Python dictionary into JSON
import json

student = {
    "name": "Alex",
    "age": 21,
    "course": "Applied Data Science"
}

json_data = json.dumps(student)  #converts the python dictionary into a JSON-formatted string.

print(json_data)                 # json.dump() = python into JSON
print("="*70)

### Step 2: JSON into python
import json

student = {
    "name": "Alex",
    "age": 21,
    "course": "Applied Data Science"
}

json_data = json.dumps(student)  #json.loads() = JSON into python

#print(json_data)

python_data = json.loads(json_data)

print(python_data)
print(python_data["name"])
print(python_data["course"])
print("="*70)

### Step 3: Write JSON to a file

with open("student.json", "w") as file:   # creates/opens a file called student.json in write mode
    json.dump(student, file, indent = 4)  # writes the python dictionary directly into the JSON file and indent = 4 makes the JSON nicely formatted ly 

print("JSON file created successfully.")
print("="*70)

### Step 4: Read JSON from a file
with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print(data["name"])
print(data["course"])
print("="*70)

### Student Data Manager
import json

student = {
    "name": "Alex",
    "age": 21,
    "course": "Applied Data Science"
}

# Save data
with open("Student.json", "w") as file:
    json.dump(student, file, indent = 4)

print("Student data saved.")

# Read data
with open("student.json", "r") as file:
    data = json.load(file)

print("Student data: ")
print("Name:", data["name"])
print("Age:", data["age"])
print("Course:", data["course"])
