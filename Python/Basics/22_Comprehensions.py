
### Step 1:List comprehension 
nums = [1, 2, 3, 4, 5]

squares = [num * num for num in nums]

print(squares)
print("="*70)

### Step 2: List comprehension with if
nums = [1, 2, 3, 4, 5, 6]

even_nums = [num for num in nums if num % 2 == 0]

print(even_nums)
print("="*70)

### Step 3: Transform + condition
nums = [1, 2, 3, 4, 5, 6]

even_squares = [num * num for num in nums if num % 2 == 0]

print(even_squares)
print("="*70)

### Dictionary comprehension 
nums = [1, 2, 3, 4, 5]

squares = {num: num * num for num in nums}

print(squares)