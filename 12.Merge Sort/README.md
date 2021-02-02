# Merget Sort

> Before start learn `Merge Sort`, let's take a look log(n)
In the computer science, log(n) is relevant to **Divide and conqure**

### Divide and conqure
- Take a bigger problem and divide into smaller problems, do it again, repeat process.
- Repeat down to smallest problems possible, solve them and work your way back toward the larger problem.

Devide and conqure, in binary terms, or dividing in half at each step
- Take a bigger item and divide by 2, next step dividing those items by 2, repeat process
- Repeat down to smallest items possible, perform whatever function you are looking to perform on the smallest items and work your way back toward the larger item

> Where this approach used?

    Sorting algorithm
    Searching algorithm
    Map - directions - take entire travel path, break it down to smaller travel paths and come up with fastest path
    Web server load - divide the load into multiple servers and service the requests

> log2(n) = x 

    x: Can be expressed as time, or complexity, number of steps/operations

> Complexity analysis

    Each level has n operation and we divided our list in two at each step to eventually get down to n lists
    this results in log(n) total steps
     
    ex) 6,8,1,4,10,7,8,9,3,2,5  (total 11 elements)
        log2(n) steps 
        log2(11) = 3.45
        -
        n operations at each step
        log(n) total steps
        n * log(n) = O(n log(n))

    Complexity: O(nlog(n))


