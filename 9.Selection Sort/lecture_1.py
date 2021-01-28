# Selection Sort  Implementation

def selection_sort(arr):
    spot_marker = 0
    while (spot_marker < len(arr)):
        for num in range(spot_marker, len(arr)):
            if arr[num] < arr[spot_marker]:
                arr[num], arr[spot_marker] = arr[spot_marker], arr[num]
        spot_marker += 1
        print(arr)


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
selection_sort(l)

# Interation step-by-step
# Start iteration 0:    6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5
# Start iteration 1:    1, 8, 6, 4, 10, 7, 8, 9, 3, 2, 5
# Start iteration 2:    1, 2, 8, 6, 10, 7, 8, 9, 4, 3, 5
# Sorted list:          1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10

