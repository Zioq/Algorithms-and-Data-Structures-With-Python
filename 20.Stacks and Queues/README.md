# Stacks and Queues

## What is a Stack?

A stack is a data structure that stores items in an Last-In/First-Out manner. This is frequently referred to as LIFO. This is in contrast to a queue, which stores items in a First-In/First-Out (FIFO) manner.

The stack is very similar to Linked lists. It just vertically listed list. 
![alt text](https://github.com/Zioq/Algorithms-and-Data-Structures-With-Python/blob/master/20.Stacks%20and%20Queues/img/stack.png)

The difference with Linked List is that the stack does not have a 'Tail' node. Because in the stack, we don't have to track Tail Node in the stack. 

In the stack, we call head as a 'Stack Pointer', and it always points top of stack.

## Common operation associated with Stack: Push, Pop, Peek, is_empty

### Push 
`Push(g)` is a functions that adds the element 'g' at the top of the stack - Time compelxity: O(1)
 
### Pop
`pop` is a functions that deletes the top most element of the stack - Time compelxity: O(1)

When we call pop, the stack pointer move down to next node which below top node, and return the value top node. 


#### Using list to create a Python Stack
The built-in list structure that you likely use frequently in your programs can be used as a stack. Instead of .push(), you can use .append() to add new elements to the top of your stack, while .pop() removes the elements in the LIFO order:

```
>>> new_stack = []
>>> new_stack.append('1')
>>> new_stack.append('2')
>>> new_stack.append('3')
>>> new_stack
['1', '2', '3']
>>> new_stack.pop()
'3'
>>> new_stack.pop()
'2'
>>> new_stack.pop()
'1'

>>> new_stack.pop()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
IndexError: pop from empty list
```

### Peek
`Peek` is a function that taking look at a value that's on top of the stack. Basically the value that stack pointer is pointing. - Time compelxity: O(1)

### is_empty
`is_empty` is a function that to check the stack is empty. That's meaning that the stack pointer points None or Null. - Time compelxity: O(1)
