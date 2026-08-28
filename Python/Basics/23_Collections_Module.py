
###Step 1: Counter
from collections import Counter

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = Counter(fruits)

print(count)

### Step 2: most_common()

print(count.most_common(2))
print("="*70)

### Step 3: defaultdict

from collections import defaultdict

student = defaultdict(int)

student["marks"] += 10
student["marks"] += 20

print(student)
print(student["marks"])
print(student["grade"])
print("="*70)

### Step 4: namedtuple
from collections import namedtuple

Student = namedtuple("Student", ["name","age","course"])

student1 = Student("Swathi", 22, "Data Science")

print(student1.name)
print(student1.age)
print(student1.course)
