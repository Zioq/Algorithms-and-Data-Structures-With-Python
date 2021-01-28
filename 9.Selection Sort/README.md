# Selection sort
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1. The subarray which is already sorted.
2. Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

## Selection sort's pros & cons
Selection sort is one of the easiest algorithms to understand. However, there is a limitation.

**Pros**

1) Selection sort can be good ate checking if everything is already sorted

2) It is also good to use when memory space is limited(This is because unlike other sorting algorithms, selection sort doesn't go around swapping thigs until the very end, resulitng in less temporary storage space used)

**Cons**

1) Selection sort is one of the slowest algorithms and can fall behind `bubble sort`
(for the large array)

## Algorithm step-by-step
Selection sort is quite slow, but it has two good sides: it is very simple and it does not require a lot of memory.

Need:
 >Marker which will move through the list on outer loop

Iteration 1 
```
1) Set marker at index 0 to start
2) Start iteration and comparisons at first element
3) Is the number at second element smaller than the number at marker?
4) If no, move to next element 
5) If yes, swap number at the element with element at marker(first element)
6) and so on
7) At the completion of first inner loop, the sublist containing 1(first element) is sorted
7) Start iteration 2, increment sopt marker by 1
8) and so on
```

Observations
```
- sublist is always sorted
- Numbers in sublist to the left of spot marker always smaller
```