# Performance measures - deep dive with a programmatic view

## Bubble Sort & Selection Sort

| Algorithm | Best Case | Average Case | Worse Case |
|:--- | :--- | :--- | :---|
| `Bubble Sort` | O(n)    | O(n^2)       | O(n^2)   |
| `Selection Sort` | O(n^2) | O(n^2)     | O(n^2)   |


## Big-0 Complexity
![alt text](https://github.com/Zioq/Python-Programming-CS-Algorithms-and-Data-Structures/blob/master/11.Performacne%20measures/big-O%20Complexity.png?raw=true) 


## How can we get the O(nlog(n)) which is better than O(n^2) ? 

| Algorithm | Best Case | Average Case | Worse Case |
|:--- | :--- | :--- | :---|
| `Bubble Sort` | O(n)    | O(n^2)       | O(n^2)   |
| `Selection Sort` | O(n^2) | O(n^2)     | O(n^2)   |
| *`Merge Sort`* | O(nlog(n)) | O(nlog(n))    | O(nlog(n))   |
| *`Quick Sort`* | O(nlog(n)) | O(nlog(n))    | O(n^2)   |
| *`Heap Sort`* | O(n)  | O(nlog(n))    | O(nlog(n))   |