# Iterators, for loops, generators, list comprehension

''' List comprehension '''

from random import randint, choice
from string import ascii_lowercase

# Generate 100 random intergers between 1 and 100
l1 =[]
for num in range(100):
    l1.append(randint(1,100))
print(l1)

# List comprehension way 
l2 = [randint(1,100) for num in range(100)]
print(l2)
print("")

l3 = [num for num in range(50)]
print(l3)
print("")

print("Generate random lowercase alphabet a-z")
l4 = [choice(ascii_lowercase) for num in range(100)]
print(l4)
