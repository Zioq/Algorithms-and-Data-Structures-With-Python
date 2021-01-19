# Dictionaries, sets and tuples

''' 
3. Sets 
- Sets are used to store multiple items in a single variable.
- A set is a collection which is both `UNORDERED` and `UNINDEXED`.
- Sets are written with curly brackets.
- Once a set is created, you cannot change its items, but you can add new items.
'''
my_set = {1, 6, 5, 'java', 'Go', 4, 45, 2, 'python', 'java'}
print(my_set) # every time position of each element is changed.

# Key feature of Sets ->  No duplicate members. Even `my_set` tuple has two 'java' element, only one 'java' is printed
print(my_set) #{1, 2, 4, 5, 6, 45, 'java', 'python', 'Go'}

my_set_1 = {1,6,2, 'java', 'Go', 8,9,10,21,1000,'python', '6'}
my_list_1 =[1,6,2, 'java', 'Go', 8,9,10,21,1000,'python', '6','python', 'Go', 21,10]
# If you wnat to delete duplicated data in the list, use `set()`
my_set_2 = set(my_list_1)
print(my_set_2) 

# how to find element in sets? -> set is unindexsed. so we cannot find element using a index.  use `in`
print('java' in my_set) # True

# Mathmatical Operation in Sets
programming_set = {'java', 'Go', 'javascript', 'python', 'php'}
print(my_set.intersection(programming_set)) # {'python', 'Go', 'java'}
print(my_set.union(programming_set)) # {1, 2, 'Go', 4, 5, 6, 'php', 45, 'javascript', 'python', 'go', 'java'}
print(my_set.difference(programming_set)) # {1, 2, 4, 5, 6, 45}

for item in my_set: #print out the element but not same order
    print(item)