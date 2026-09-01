
#def nums():
 #   return [1,2,3,4,5]

### Generator
def nums():
    for i in range(1,6):
        yield i

for num in nums():
    print(num)
print("="*70)

### Practice
def even_nums():
    for i in range(2, 11, 2):
        yield i

for num in even_nums():
    print(num)
