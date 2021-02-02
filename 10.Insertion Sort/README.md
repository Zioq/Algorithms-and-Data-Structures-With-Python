# Insertion sort
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. 

The array is virtually split into a sorted and an unsorted part. 

Values from the unsorted part are picked and placed at the correct position in the sorted part.

At the beginning, the sorted subarray contains only the first element of our original array.
The first element in the unosrted array is evaluated so that we can insert it into its proper place in the sorted subarray.
The insertion is done by moving all elements larger than the new element one posision to the right. 
Continue doing this until our entire array is sorted. 

## Algorithm step-by-step
To sort an array of size n in ascending order:
1. Iterate from `arr[1]` to `arr[n]` over the array
2. Compare the current element (key) to its predecessor.
3. If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.