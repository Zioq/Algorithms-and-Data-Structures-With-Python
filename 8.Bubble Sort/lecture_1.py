# Bubble sort 
''' 
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. 

[Complexity]
we itertated through n elements so it terms of complexity we get n for the n elements 
-> O(n^2)
'''

# Bubble sort implementation

def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        print("Bubble sort status: " + str(arr))
        swap_happened = False
        # we don't have to compare last element, so set len(arr)-1
        for num in range(len(arr)-1):
            if(arr[num] > arr[num+1]):
                # Python's dynamic assign element method
                # arr[0], arr[1] = arr[1], arr[0]
                #print("Swap happened")
                swap_happened = True 
                arr[num], arr[num+1] = arr[num+1], arr[num]


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l)

# Bubble sort implementation step-by-step
# Start iteration 0:    6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5
# after iterstion 1:    6, 1, 4, 8, 7, 8, 9, 3, 2, 5, 10
# after iteration 2:    1, 4, 6, 7, 8, 8, 3, 2, 5, 9, 10
# ...
# sorted list :         1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10
