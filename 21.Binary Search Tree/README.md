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
- 
![alt text](https://github.com/Zioq/Algorithms-and-Data-Structures-With-Python/blob/master/21.Binary%20Search%20Tree/img/BinarySearchTrees.png)
>As you can see, the left side of root(50) all nodes' value are less than 50 and the right side of root(50) all nodes' value are larger than 50. 

#### Binay Search Tree(BST) are powerful
- Search: O(h)
- Insert: O(h)
- Delete: O(h)
- h = Height of the tree

BST' do allow for this to happen 
> ![alt text](https://github.com/Zioq/Algorithms-and-Data-Structures-With-Python/blob/master/21.Binary%20Search%20Tree/img/bst.png)
> It's looks like Lined List. For this reason, O(n) is same with O(h) (h: number of nodes).
> 
> In such cases: search, insder and delete will al be O(n) which is worst case for BST
