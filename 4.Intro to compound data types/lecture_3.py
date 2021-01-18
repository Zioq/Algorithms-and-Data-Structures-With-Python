# Lists - an in-depth look 2

my_list = [16, 8, 4, 7, 12, 6, 19, 30, 4]
my_string_list = ["comp sci", "physics", "elec engr", "philosopy"]
my_new_list = ["art", "economic"]
print(f"Ints: {my_list}")
print(f"Strings: {my_string_list}")

# Adding / Remove
# append(), insert(), extend()
print("Add/remove...")

# append() -> add element in the last position in a list 
# Cannot be assigned in new variable
my_list.append(25) #[16, 8, 4, 7, 12, 6, 19, 30, 4, 25]
print(my_list)

# insert() -> add element where you want to put in the list
my_list.insert(4, 777) #.insert(index, newData)
print(my_list) # [16, 8, 4, 7, 777, 12, 6, 19, 30, 4, 25] 

# extend() -> add another list element in the exists element 
''' 
Big difference append() and extend()
my_string_list.append(my_new_list)
print(my_string_list) 
['comp sci', 'physics', 'elec engr', 'philosopy', ['art', 'economic']] 
'''
# Cannot be assigned in new variable
my_string_list.extend(my_new_list)
print(my_string_list) #['comp sci', 'physics', 'elec engr', 'philosopy', 'art', 'economic']

# Remove element 
# pop(), remove()

# remove() method takes a single element as an argument and removes it from the list.
my_string_list.remove("comp sci") 
print(my_string_list) #['physics', 'elec engr', 'philosopy', 'art', 'economic']
# pop() list.pop(index)  The pop() method returns the item present at the given index. This item is also removed from the list.
print(my_string_list.pop()) # last element will be removed if there is noe arguement 
print(my_string_list) #['physics', 'elec engr', 'philosopy', 'art']

my_list_2 = [16, 8, 4, 7, 12, 6, 19, 30, 4]
#indices     0   1  2  3  4   5   6   7  8
my_string_list_2 = ["comp sci", "physics", "elec engr", "philosopy"]
print(my_list_2[-1])
#my_list_2[-1] = 1000
#print(my_list_2) # [16, 8, 4, 7, 12, 6, 19, 30, 1000]

#slicing 
print(my_list_2[0:4]) #[startPoint : LastPointButNotIncluded]
print(my_list_2)
print(my_list_2[::2]) #[startPoint : LastPointButNotIncluded : StepSide]
print(my_list_2[::-1]) #moving back by 1 #[4, 30, 19, 6, 12, 7, 4, 8, 16] -> reversed list
# same reverse method in list
#my_list_2.reverse()
print(my_list_2)

# iteration
for item in my_list_2:
    print(item)