
for i in range(5):
    print(i)
print("=" *20)

for i in range(1,5):
    print(i)                    #range(start, stop)
print("=" *20)

for i in range(1,10,2):
    print(i)                    #range(start, stop, step)
print("=" *20)

#While loop

count = 1

while count <= 5:
    print(count)
    count += 1                # += is used to increment the value of count by 1
print("=" *20)

#Practice 1
print("Reverse counting")
for i in range(5, 0, -1):
    print(i)
print("=" *20)

#Nested loops basic

for i in range(3):
    for j in range(2):
        print(i,j)
print("=" *20)

#Mission challenge
print("Mission Challenge")
name = input("Enter your name: ")
for i in range(5):
    print(f"Welcome {name}!")

#bonus challenge 
print("Bonus Challenge")
num = int(input("enter a number: "))
for i in range(1, num+1):
    print(i)
