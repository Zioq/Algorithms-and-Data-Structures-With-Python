# Insertion Sort Implementation

def insertion_sort(arr):
    # Always set the key index as 1 in insertion sort
    for key in range(1, len(arr)):
        if arr[key] < arr[key-1]:
            j = key
            while j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1] , arr[j]
                j -= 1
    print(arr)

l = [6, 1, 8, 4, 10]
insertion_sort(l)