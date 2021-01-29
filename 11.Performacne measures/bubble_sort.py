# Bebbule sort's total comparison number
def bubble_sort(arr):
    swap_happended = True
    comparison = 0
    while swap_happended:
        comparison += 1
        print('Bubble sort status: ', str(arr))
        swap_happended = False
        for num in range(len(arr)-1):
            comparison += 1
            if arr[num] > arr[num+1]:
                swap_happended = True
                arr[num], arr[num+1] = arr[num+1], arr[num]
    print('Comparison: ', comparison)


original_case = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]  # Original case
worst_case = [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1]  # Worst case
best_case = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10] # Best case 

print("Original Case")
bubble_sort(original_case)
print("-"*30)
print("Worst Case")
bubble_sort(worst_case)
print("-"*30)
print("Best case")
bubble_sort(best_case)
