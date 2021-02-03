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
