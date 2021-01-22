# Functions - execution context, frames, mutable vs. immutable arguments in-depth

'''[Program] for immutable data type which is integer'''
def func_0(start_num):
    start_num += 1
    return func_1(start_num)

def func_1(start_num):
    start_num += 1
    return start_num

start_num = 1
print(f"start_num\t -> {start_num}")
finish_num = func_0(start_num)
print(f"calc'd_num\t -> {finish_num}")
print(f"start_num\t -> {start_num}")
'''
start_num	 -> 1
calc'd_num	 -> 3
start_num	 -> 1
'''

''' [Grobal Frame]

Function objects:
func_0
func_1

int objects:
start_num -> 1

finish_num -> 3 (get 3 after finish func_1 Frame)
'''


''' [func_0 Frame]
start_num -> 1
start_num -> 2 (after incremented by the code 'start_num +=1')

return 3 (get 3 after finish func_1 Frame)
'''

''' [func_1 Frame]
start_num -> 2 (retuned value from func_0 Frame)
start_num -> 3 (after incremented by the code 'start_num+1')
'''

print("")
'''[Program] for mutable data type which is list'''
def func_0(other_num):
    other_num[0] += 1
    return func_1(other_num)

def func_1(another_num):
    another_num[0] += 1
    return another_num

start_num = [1] # start_num is a list with integer 1 as value index is 0
print(f"start_num\t -> {start_num}")
finish_num = func_0(start_num)
print(f"calc'd_num\t -> {finish_num}")
print(f"start_num\t -> {start_num}")
print(finish_num ==start_num) # True since they referencing same list object 
''' [Global frame]

function objects:
func_0
func_1

list objects:
start_num -> [1]


finsih_num -> reference list object which has incremented (After finish `func_0`)

At last, the finish_num & start_num are pointing to same list object that has a value 3 in the 0 index 

'''

''' [List object (outside of Global frame)]
Reference work differently when you pass in variable(start_num) as a paramter to function call 
'''

''' [func_0 frame]
other_num -> used as reference object. so other_num pointing same list object  which is pointed `start_num in Global frame (Since it's reference)

So, other_num does not have its own copy of the list(start_num)
After code `other_num[0] +=1`, now our list object has a value 2 in the 0 index

With the list object which has a value 2 in the 0 index, execute func_1
'''

''' [func_1 frame]
This func_1 function is referencing same list object, which has a value 2 in the 0 index
After code `another_num[0] +=1`, now our list object has a value 3 in the 0 index
At the last, this function return this list obect reference `return another_num`. So, returned value is a reference to the list obejct
'''


print("")
def func_0(other_num):
    other_num[0] += 1
    return func_1(other_num)

def func_1(another_num):
    another_num[0] += 1
    return another_num

start_num = [1] # start_num is a list with integer 1 as value index is 0
print(f"start_num\t -> {start_num}")
finish_num = func_0(start_num.copy()) # When you invoke func_0, you could pass copy of start_num list, insted of reference to the list itself
print(f"calc'd_num\t -> {finish_num}")
print(f"start_num\t -> {start_num}")
print(finish_num ==start_num) # False

print("")
def func_0(other_num):
    other_num[0] += 1
    return func_1(other_num)

def func_1(another_num):
    another_num[0] += 1
    return another_num

start_num = [1] # start_num is a list with integer 1 as value index is 0
print(f"start_num\t -> {start_num}")
finish_num = func_0(start_num[:]) # Slice whole list 
print(f"calc'd_num\t -> {finish_num}")
print(f"start_num\t -> {start_num}")
print(finish_num ==start_num) # False