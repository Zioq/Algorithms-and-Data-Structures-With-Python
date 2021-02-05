# Bisection search - recursive implementation

def bisection_recur(n, arr, start, stop):
    # Set the base case first
    if start > stop:
        return (f"{n} not found in list")
    else:
        mid = (start + stop) // 2
        if n == arr[mid]:
            return (f"{n} found at index: {mid}")
        elif n > arr[mid]:
            start = mid + 1
            return bisection_recur(n, arr, start, stop)
        else:
            stop = mid - 1
            return bisection_recur(n, arr, start, stop)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #ind 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
n = 8
print(bisection_recur(8, l, 0, len(l)-1))
print("\n")

for num in range(16):
    print(bisection_recur(num, l, 0, len(l)-1))
