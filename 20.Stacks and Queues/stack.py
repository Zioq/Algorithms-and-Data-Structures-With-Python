import time

class Node:

    def __init__(self, data = None):
        ''' Initialize node with data and next pointer '''
        self.data = data
        self.next = None

    
class Stack:

    def __init__(self):
        ''' Initialize stack with stack pointer '''
        print("Stack created")
        # Only add stack pointer which is Head
        self.stack_pointer = None

    # Push - can only push (add) an item on top of the stack (aka head or stack pointer)
    def push(self,x):
        ''' Add x to the top of stack '''
        if not isinstance(x, Node):
            x = Node(x)
        print (f"Adding {x.data} to the top of stack")
        # If the Stack is empty, set the stack point as x, which is just added.
        if self.is_empty():
            self.stack_pointer = x
        # If the Stack has some Node
        else:
            x.next = self.stack_pointer
            self.stack_pointer = x
                
    # Pop - can only remove an item on top of the stack (aka head or stack pointer)
    def pop(self):
        if not self.is_empty():
            print("Removing node on top of stack")
            curr = self.stack_pointer
            self.stack_pointer = self.stack_pointer.next
            curr.next = None
            return curr.data
        else:
            return "Stack is empty"    

    def is_empty(self):
        '''return True if stack is empty, else return false'''
        return self.stack_pointer == None

    # peek - view value on top of the stack (aka head or stack pointer)
    def peek(self):
        '''look at the node on top of the stack'''
        if not self.is_empty():
            return self.stack_pointer.data

    def __str__(self):
        print("Printing Stack state...")
        to_print = ""
        curr = self.stack_pointer
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            print("Stack Pointer")
            print(" |")
            print(" V")
            return "[" + to_print[:-2] + "]"
        return "[]"

my_stack = Stack()
print("Checking if stack is empty:", my_stack.is_empty())
my_stack.push(1)
time.sleep(2)
my_stack.push(2)
print(my_stack)
time.sleep(2)
my_stack.push(3)
time.sleep(2)
my_stack.push(4)
time.sleep(2)
print("Checking item on top of stack:", my_stack.peek())
time.sleep(2)
my_stack.push(5)
print(my_stack)
time.sleep(2)
print(my_stack.pop())
time.sleep(2)
print(my_stack.pop())
print(my_stack)
time.sleep(2)
my_stack.push(4)
print(my_stack)
time.sleep(2)