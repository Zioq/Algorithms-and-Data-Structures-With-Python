# Selection sort's total comparison number
def selection_sort(arr):
    spot_marker = 0
    comparison = 0
    while spot_marker < len(arr):
        comparison += 1
        for num in range(spot_marker, len(arr)):
            comparison += 1
            if arr[num] < arr[spot_marker]:
                arr[spot_marker], arr[num] = arr[num], arr[spot_marker]
        spot_marker += 1
    print('Comparison: ', comparison)

original_case = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]  # Original case
worst_case = [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1]  # Worst case
best_case = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10] # Best case 

print("Original Case")
selection_sort(original_case)
print("-"*30)
print("Worst Case")
selection_sort(worst_case)
print("-"*30)
print("Best case")
selection_sort(best_case)

''' 
Selection sort even though has same case of bubble sort, the number of comparison is slightly less.
Becuase of number of comparison being less each iteration after first run in selection sort
 '''