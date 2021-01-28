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
- After a fiew iterations, you'll get to this state: Marker moves up one spot and the spot marker will no loger be less than lenghth of array
```

## Complexity analaysis
As we ran through each inner loop, we iterated through `n` elements since our list has `n` elements.

So in terms of complexity we get `n for n` elements(`inner loop`)

But this only resulted in 1 sorted element out of list.

In terms of complexity we get `n for n` elements(`inner loop`)

So we did it again for each of our `n` element(moving the marker by 1)

Resulting in an outer loop which ran through n elements

In terms of complexity we get `n for n` element (`inner loop`)

In terms of complexity we g et `n for n` elements (`outer loop`)

So combined we get `complexity` of n * n, or `O(n^2)`
```
But each time in our inner loop we had moved up the spot marker by 1.
Resulting in n-1 on the second run, and n-2 in the third run and so on
So why are we still using n(which is whole length of the list)?
It's becuase when working with complexity you drop the lower order term n-1 becomes n, simply because the higher order terms have more impact. 
```
