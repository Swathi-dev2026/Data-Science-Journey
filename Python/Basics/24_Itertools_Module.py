
### Step 1: count()
from itertools import count

counter = count(1)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print("="*70)

### Step 2: cycle()
from itertools import cycle

colors = cycle(["Red", "Green", "Blue"])

print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print("="*70)

### Step 3: repeat()
from itertools import repeat

values = repeat("Python", 3)

for value in values:
    print(value)