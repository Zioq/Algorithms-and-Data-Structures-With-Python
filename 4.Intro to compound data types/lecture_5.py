# Dictionaries, sets and tuples

''' 
2. Tuple 
- Tuples are used to store multiple items in a single variable.
- A tuple is a collection which is ordered and `UNCHANGEABLE`.
- Tuples are written with `ROUND BRACKETS`.
'''

my_random_tuple = ('first', 1, 4, 3, 5, 4, 'hello world', 12, 5, 5, 34, 45)
my_tuple = ('first_value', 'second_value', 'third_value')

print(my_random_tuple[0])  # first
print(my_random_tuple[-1])  # 45
print(my_random_tuple[::-1])

# check how many element in the tuple -> len()
print(len(my_random_tuple))  # count `10`

# count how many specific element in tuple -> count('value')
print(my_random_tuple.count(5)) # 3

# find index location of element in tuple -> index('value')
print(my_random_tuple.index('hello world')) # index 6 

# The power of tuple. We can assign tuple element in a new variable
first_var, second_var, third_var = my_tuple
print(first_var) # We can check the first element of my_tuple, which is `first_value` is saved in a new variable `first_val`

for item in my_tuple:
    print(item)