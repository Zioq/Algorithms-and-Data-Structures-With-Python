def quicksort(arr):
    ''' 
    Input: Unsorted list of integers
    Returns sorted list of integers using Quicksort
    Note: This is not an in-place implementation 
    '''

    # set base-case
    if len(arr) < 2:
        return arr
    else:
        #set the pivot(last element in the list)
        pivot = arr[-1] 
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        #to prevent return tuple format, and return as one list item
        return quicksort(smaller) + equal + quicksort(larger) 


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
print(quicksort(l))