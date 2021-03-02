# Introduction to Trees and Binary Search Trees - Non-linear representations of data

## Tree node data structure
![alt text](https://github.com/Zioq/Algorithms-and-Data-Structures-With-Python/blob/master/21.Binary%20Search%20Tree/img/binary_tree.jpg)

## What is a tree data structure?
Tree represents the nodes connected by edges. It is a non-linear data structure. It has the following properties.
- One node is marked as Root node.
- Every node other than the root is associated with one parent node.
- Each node can have an arbiatry number of chid node.

### Key Rules: 
* Can't have cycles. A->B->E->A not allowed
* Can't have mutiple parents. 
* There can only be 1 root in a tree
* Root can't point to itself

### Height of a tree:
Number of levels to leaf nodes starting from the root node.

### Uses of tree structures
* They're everywhere in computing.
* Think of organizational charts, those are all tree(cna a boss be the boss of themselves? can an employee be the boss's boss? can a team member be the project manager's manager?).
* The unix file system(the command line) is a tree structure, starting with the root directory , aptly named 'root'
* Decision tree are very popular in ML, a lot of algorithms are trying to 'learn' what decision to take at every level of the tree to arrive at the right outcome. 

### Binary Tree
In the binary tree, each node can only have max 2 children(left and right)

**Rules in Binary Tree**
- Each node on left of current node has to be smaller in value.
- Each node on right of current node has to be larger in value. 
