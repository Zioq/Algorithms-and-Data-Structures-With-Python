
def bubble_sort(arr):
    for i in range(len(arr)-1):  # first iteration
        if(arr[i] > arr[i+1]):
            print("Swap happend")
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(arr)
        print("-"*30)

def bubble_sort_flag(arr):
    swap_happened = True
    while swap_happened:
        print("Bubble sort status: "+ str(arr))
        swap_happened = False            
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                swap_happened = True
                arr[i], arr[i+1] = arr[i+1], arr[i]
        print("-"*30)
    print("*"*30)


l = [5, 4, 3, 2, 1]
print("The first iteration mechanism in Bubble Sort")
bubble_sort(l)
print("\n")
print("The whole iteration mechanism in Bubble Sort with flag")
bubble_sort_flag(l)


