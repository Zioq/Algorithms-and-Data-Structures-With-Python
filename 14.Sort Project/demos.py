print("Algorithms file loaded")

# Quick Sort Algorithm
def quickSort(arr):
    if len(arr) <  2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num  == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quickSort(smaller) + equal + quickSort(larger)

# Merge Sort Algorithm
def merge_sorted(arr1,arr2):
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j <len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1 
        else: 
            sorted_arr.append(arr2[j])
            j += 1
    while i<len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j<len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

def mergeSort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = mergeSort(arr[:middle])
        l2 = mergeSort(arr[middle:])
        return merge_sorted(l1,l2)

# Bubble Sort Algorithm
def bubbleSort(arr):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]