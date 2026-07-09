
fruits = ["Apple", "Banana", "Orange"]
print(fruits)

# Indexing
print(fruits[0])
print(fruits[1])
print("="*50)

# Changing an item
fruits[1] = "Mango"
print(fruits)
print("="*50)

# Adding an Item
fruits.append("Grapes")
print(fruits)
print("="*50)

# removing an item
fruits.remove("Orange")
print(fruits)
print("="*50)

# Length
print(len(fruits))
print("="*50)

# Loop through a list
for fruit in fruits:
    print(fruit)
print("="*50)

# Challenge 1
print("Challenges")
programming_languages = ["python","java","SQL","numpy","pandas"]
print(programming_languages)
print("="*50)

# Challenge 2
print (programming_languages[3])
print("="*50)

# challenge 3
programming_languages[1] = "scikit"
print(programming_languages)
print("="*50)

# challenge 4
programming_languages.append("javascript")
print(programming_languages)
print("="*50)

# challenge 5
programming_languages.remove("python")
print(programming_languages)
print("="*50)

# challenge 6
print(len(programming_languages))
print(programming_languages)
print("="*50)

# Bonus challenge
print("Bonus Challenge")
for language in programming_languages:
    print(f"I want to learn {language}")