
### step 1: Find a pattern
import re

text = "My phone number is 9872341243."

result = re.search(r"\d+", text)

print(result.group())
print("="*70)

### step 2: Find all numbers
import re

text = "I have 2 cats, 3 dogs and 20 fish."

nums = re.findall(r"\d+", text)

print(nums)
print("="*70)

### step 3: Find words
import re

text = "Python is powerful and Python is useful."

result = re.findall(r"Python", text)

print(result)
print(len(result))
print("="*70)

### step 4: Find an email address
import re

text = "Contact me at swathi@example.com"

pattern = r"\w+@\w+\.\w+"

result = re.search(pattern, text)

print(result.group())
print("="*70)

### step 5: one last imp regex concept: \w+
import re

text = "Emails: swathi@gmail.com and akash@yahoo.com"

emails = re.findall(r"\w+@\w+\.\w+",text)

print(emails)
print("="*70)

### Practice
import re

text = "My name is Swathi. My age is 22. Contact: swathi@gmail.com"

#Find the age
age = re.search(r"\d+",text)

#Find the email
email = re.search(r"\w+@\w+\.\w+", text)

print("Age:", age.group())
print("Email:", email.group())