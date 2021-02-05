# Binary Search

`Binary` is a technique dividing a collection of elements into two halves and remove one of them at each step of algorithm.

This can dramatically reduce the number of comparisons required to find an element.
> BUT HERE IS A REQUISITE
    elements in the collection must be `sorted` first

This idea very similar to find a page in a book. If we want to find a specific page, we randomly open the book and when the page number is less than the page must be to the right, vice versa

To minimizes the number of tries, pick the middle of pages in the book and repeat that process. 

This binary search algorithm use a `divide-and-conquer` technique, so this performance follows O(log n).