# While loops, enumerate, zip

# while loops
# break (and pass) keyword
# generator - zip function

from random import  randint
truth_condtion  = True

# Do while condition is True. Stop the loop when condition is False, or meet the `break` in while loop

i = 0
while i < 10:
    print(i)
    i +=1

print("")
l1 = [randint(1,100) for num in range(1000)]
index=0
num_to_search = 25
while index<len(l1):
    if l1[index] == num_to_search:
        print(f"{num_to_search} found at index: {index}")
    index +=1
print("")

print("If you want to get only first result, Add break")
l1 = [randint(1,100) for num in range(1000)]
index=0
num_to_search = 25
while index<len(l1):
    if l1[index] == num_to_search:
        print(f"{num_to_search} found at index: {index}")
        break
    index +=1

print("")
print("Using a for loop")
l1 = [randint(1,100) for num in range(1000)]
index=0
num_to_search = 25
for num in l1:
    index +=1 
    if num == num_to_search:
        print(f"{num_to_search} found at index: {index}")
        break

# numerate() function 
# The enumerate() method adds counter to an iterable and returns it (the enumerate object).
# enumerate(iterable, start=0)
print("")
print("Using a enumerate function")
l1 = [randint(1,100) for num in range(1000)]

num_to_search = 25
for index, num in enumerate(l1):
    if num == num_to_search:
        print(f"{num_to_search} found at index: {index}")
        break


while True:
    print("Please choose an option form the list below")
    print("Press 1 for selection 1")
    print("Press 2 for selection 2")
    print("Press 3 for quit")
    selection = input("Enter your choice: ")
    if(int(selection)==3):
        break