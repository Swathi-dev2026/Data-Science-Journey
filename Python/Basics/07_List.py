
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