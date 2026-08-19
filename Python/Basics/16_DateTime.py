
# step1: Get today's date
from datetime import date

today = date.today()

print("Today's date:", today)
print("="*50)

# step2: current date and time
from datetime import datetime

now = datetime.now()

print("Current date and time:", now)
print("="*50)

# step3: extract individual parts
from datetime import datetime

now = datetime.now()

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:",now.second)
print("="*50)

#step4: Formatting dates
from datetime import datetime

now = datetime.now()

formatted_date = now.strftime("%d-%m-%Y") #%d = day, %m = month, %Y = 4 digit year

print("Formatted date:", formatted_date)
print("="*50)

# AGE CALCULATOR
from datetime import date

birth_year = int(input("Enter your birth year: "))

current_year = date.today().year

age = current_year - birth_year

print("Your approximate age is:", age)