# Quicksort: fan favorite

| Algorithm | Best Case | Average Case | Worst Case |
|:--- | :--- | :--- | :---|
| *`Merge Sort`* | O(nlog(n)) | O(nlog(n))    | O(nlog(n))   |
| *`Quick Sort`* | O(nlog(n)) | O(nlog(n))    | O(n^2)   |

Even the worst case in `Quick sort` is much slower than `Merge sort`, `Quick Sort` is preferred. This is because that worst case is very very rare. 

Also, in terms of overall performance, actual runtime of quick sort has to be better than the merge sort.

## Why Quick Sort is preferred over MergeSort for sorting Arrays

- Space Complexity: Quick Sort require only O(logN) stack space whereas Merge Sort requires O(N) extra storage for array.

- Time Complexity: Allocating and de-allocating the extra space used for merge sort increases the running time of the algorithm. Comparing average complexity we find that both type of sorts have O(NlogN) average complexity but the constants differ.

### Implementation step-by-step
1. Step 1: Find a pivot, can be random item from the list. A popular choice is to pick the first or last element.
2. Step 2: 
    a. Arrange all items smaller than pivot to the left of pivot
    b. Arrange all itmes larger than the pivot to the right of the pivot
    c. If there are equal items to the pivot, arrange them in the middle

> Exmaple
    6, 8, 1, 4, 10 ,7 ,8 ,9, 3, 2, 5
    Set pivot : 5

    <After Arrange>
    1, 4, 3, 2, 5, 6, 8, 10, 7, 8, 9

    <All itmes to the left of 5 are less than 5>
    1, 4, 3, 2

    <All itmes to the right of 5 are larger than 5>
    6, 8, 10, 7, 8, 9

    <`5` is middle>

    <We have 3 lists>
    Smaller list: 1, 4, 3, 2 
    Equal list: 5
    Larger list: 6, 8, 10, 7, 8, 9

    <Run same algorithm on smaller list & Larget list each on and on >
