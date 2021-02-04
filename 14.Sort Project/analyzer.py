import time
import random
from demos import quicksort
from demos import mergeSort



def create_random_list(size,max_val):    
    rand_list = []
    for num in range(size):
        rand_list.append(random.randint(1,max_val))
    return rand_list


size = int(input("What size list do you want to create? "))
max_val = int(input("What is the max value of the range? "))

l = create_random_list(size,max_val)
tic = time.time()
quicksort(l)
toc = time.time()
print("QS Elapsed time -> ", toc-tic)

tic = time.time()
mergeSort(l)
toc = time.time()
print("MS Elapsed time -> ", toc-tic)