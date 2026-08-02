
skills = {"Python", "SQL", "Pandas", "Python", "SQL"}
print(skills)
print("="*50)

# Adding to a set

skills = {"Python", "SQL", "Pandas"}
skills.add("Numpy")
print(skills)
skills.add("Python")   # This will not add a duplicate
print("="*50)

# removing an item

skills = {"Python", "SQL", "Pandas"}
skills.remove("SQL")
print(skills)
print("="*50)

# set length
skills = {"Python", "SQL", "Pandas", "Numpy"}
print(len(skills))
print("="*50)

# discard() method

skills = {"Python","SQL", "Pandas"}
skills.discard("java")  
print(skills)
print("="*50)

# set union

pyhton_Skills = {"Python", "Pandas", "NumPy"}
data_skills = {"Sql", "Pandas", "Power BI"}

all_skills = pyhton_Skills.union(data_skills)
print(all_skills)
print("="*50)

# set intersection

python_skills = {"python", "pandas","numpy"}
data_skills = {"sql", "pandas", "power bi"}

commomn_skills = python_skills.intersection(data_skills)
print(commomn_skills)
print("="*50)

# Difference of sets

python_skills = {"python", "pandas","numpy"}          #difference() gives you the items that are in the first set but not in the second set.
data_skills = {"sql", "pandas", "power bi"}

result = python_skills.difference(data_skills)
print(result)
print("="*50)

# reverse difference of sets

result = data_skills.difference(python_skills)
print(result)
print("="*50)

# in with sets

skills = {"Python", "SQL", "Pandas"}

if "Python" in skills:
    print("Python is available")
else:
    print("Pyhton is not available")
print("="*50)

# practice

python_skills = {"Python", "Pandas", "NumPy"}
data_skills = {"SQL", "Pandas", "Power BI"}

common = python_skills.intersection(data_skills)
unique_python = python_skills.difference(data_skills)

print("Common skills:", common)
print("Python-only skills:", unique_python)

if "Pandas" in common:
    print("Pandas is a common skill")