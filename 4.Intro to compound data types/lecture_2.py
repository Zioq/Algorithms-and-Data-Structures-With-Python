# Lists - an in-depth look 1
''' 
1. Sort - sort(), sorted() : Nice prep for algorithm section
2. Find - len(), min(), max(), in, indexing, slicing, count()
3. Insert/remove - append(), insert(), extend(), remove(), pop()
4. Sub-lists - sliocing, in-place, copying
5. Iteration - for loops, while loops 
 '''

my_list = [16, 8, 4, 7, 12, 6, 19, 30,4]
my_string_list = ["comp sci", "physics", "elec engr", "philosopy"]

print(id(my_list)) #4341181576
print(f"Ints: {my_list}")
print(f"Strings: {my_string_list}")

# Sort Integers in list: sorted()
sorted_list = sorted(my_list)
print("Sorting...")
print(sorted_list)

# Use method for sort: sort() -> We don't need a new variable to save sorted list
my_list.sort()
print("Use sort() method")
print(f"Sorted Ints: {my_list}")

# When we use sorted(), this re-assign the sorted list in a new variable memeory. But sort() method, sort the list element in the same list, that means new variable does not need and use same memeory location.
print(id(sorted_list)) #4341188168
print(id(my_list)) #4341181576

# `in` -> Give True / False for data exists in the list or not
print("Finding Info...")
print("physics" in my_string_list) #True
print(30 in my_list) #True

# .index() -> find out the element index number in list
print(my_string_list.index("physics")) # return 1

# len() -> return list lenght
print(len(my_list)) # return 8 
print(my_list[-1]) # return last element in list 

# min() -> return minimu element in list
print(min(my_list))

# max() -> return maximum element in list
print(max(my_list))

# count() -> return how many same data exists in the list
print(my_list.count(4))