
import numpy as np

zeros = np.zeros(5)
ones = np.ones(5)

print("Zeros: ", zeros)
print("Ones: ", ones)
print("="*70)

# arrange()

nums = np.arange(1, 11)

print(nums)
print("="*70)

# linespace()

nums2 = np.linspace(0, 1, 5)  # 5 evenly spaced numbers between 0 and 1

print(nums2)
print("="*70)

# random()

random_nums = np.random.randint(1, 101, 5)  # 5 random integers between 1 and 100)

print("Random:", random_nums)
print("="*70)

