
### Step 1: Iterator
nums = [10,20,30]

iterator = iter(nums)   # creates iterator

print(next(iterator))   # gets next item
print(next(iterator))
print(next(iterator))
print("="*70)

### Step 2: What happens when there are no more items?
nums = [10,20,30]

iterator = iter(nums)   # creates iterator

print(next(iterator))   # gets next item
print(next(iterator))
print(next(iterator))
#print(next(iterator))
print("="*70)

### Step 3: Generators
def count_nums():
    yield 1   # yield pauses the function and remembers where it stopped
    yield 2
    yield 3

nums = count_nums()

print(next(nums))
print(next(nums))
print(next(nums))
print("="*70)

### Step 4: Generator with a for loop
def count_nums():
    yield 1
    yield 2
    yield 3

for num in count_nums():
    print(num)
print("="*70)

### Practical Exercise
def even_nums(limit):
    for num in range(2, limit + 1, 2):
        yield num
for num in even_nums(10):
    print(num)