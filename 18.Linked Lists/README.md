# linear data structures - Linked Lists
## Linked Lists

A linked list is a `linear data structure`, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.

![alt text](https://github.com/Zioq/Algorithms-and-Data-Structures-With-Python/blob/master/18.Linked%20Lists/img/Linkedlist.png?raw=true) 

## Linked Lists and 'Node'
Linked list is a `list of nodes` (you can think node as an object). So if you want to add some integer data into linked list, you have to convert the data into node data like this.

![alt text](https://github.com/Zioq/Algorithms-and-Data-Structures-With-Python/blob/master/18.Linked%20Lists/img/linkedlistnode.png?raw=true) 

A node in a Linked List is consist of `data` and `pointer`

Data: contains the data for the nede, example - Integers, Strings, other objects etc.

Pointer: points to next node in the list

## Singly Linked List
![alt text](https://github.com/Zioq/Algorithms-and-Data-Structures-With-Python/blob/master/18.Linked%20Lists/img/singlylistedlist.png?raw=true) 

This is a singly linked list where the nodes are pointing one direction. Staring with a `Head`, you can only have ONE Head in a linked list. Also, you need to think about 'Linear' terms. Because there is no random access, since none of node are index. There is no index unlike other dynamic structure. 

## Construction of Linked List
1. At first, basically you will create linked list object and it would be empty. (Only has `Head` points None and `Tail` points None)
2. When you have a item to add linked list, you will convert it to node if not node already.
3. When we add first node element in the linked list, that node will be a 'Head' and the pointer will be None. Because this node is a first and last node element in the linked list.
    ![alt text](https://github.com/Zioq/Algorithms-and-Data-Structures-With-Python/blob/master/18.Linked%20Lists/img/firstelement.png?raw=true) 
4. Now, we have another item to add in the linked list. If the item is not node object, let's convert it first. First, make `Head pointer` point this second node element. And then this next pointer will be None. Becuase it will be last node element in the linked list. 
    ![alt text](https://github.com/Zioq/Algorithms-and-Data-Structures-With-Python/blob/master/18.Linked%20Lists/img/secondelement.png?raw=true) 
5. We add one more item to add in the linked list. What you do is iterate through staring from head, you look at the list to the first node has pointer point None, and you simply point it to the new added node item. And next, the added node pointer will have pointer points None. 

### Add operation
- O(1) if you keep track of tail node
- O(n) if you don't keep track of tail, since you have to iterate through all nodes to find last node(next pointer points to None for last node)
- O(1) of you add to front(left) of the list since you always keep track of head node

### Remove operation
- O(1) if you remove from head
- O(n) if you remove from right (end of list)

### Remove from tail/end
- O(n) - iterate through list till you are in the node prior to the tail or last node (current_node.next == tail), set current_node.next = None and set tail to point to current node.
- O(n) - if you don't track tail, keep track of previous node and current node as you iterate through the list, when you get to current_node.next == None (last node), set the previous node.next = None

### Some notes on Linked Lists
* There's no random access, ex) you can't jump to the nth element if you choose to unlike an array.
* Most operation, except for ones that take place with head or tail noes of the list, are sequential.
* Since there is no predetermined or default size in a list, there is no pre-allocation of memory, and each node can be created and added as necessary.