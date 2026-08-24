
### Step 1: Lambda

square = lambda x: x * x

print(square(8))
print("="*70)

### Step 2: map()

nums = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x*x, nums))

print(squares)
print("="*70)

### Step 3: filter()

nums = [1, 2, 3, 4, 5, 6]

even_nums = list(filter(lambda x: x % 2 == 0, nums))

print(even_nums)
print("="*70)

### Quick Practice

nums = [1, 2, 3, 4, 5, 6]

even_nums = filter(lambda x: x % 2 ==0, nums)

square_nums = list(map(lambda x: x * x, even_nums))

print(square_nums)