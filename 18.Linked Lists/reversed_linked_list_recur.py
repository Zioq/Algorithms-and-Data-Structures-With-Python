# Reversed Linked List (Recursive)
class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_val(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def __str__(self):
        to_print = ""
        current = self.head
        while current is not None:
            to_print = to_print + str(current.data) + "->"
            current = current.next
        if to_print:
            return "[" + to_print[:-2] + "]"
        return "[]"

    def reverse_list_recur(self, current, previous):
        ''' reverse the sequence of node pointers in the linked list '''
        # Given [1->2->3->4->5] reverse pointers [1<-2<-3<-4<-5]
        # Turning list to [5->4->3->2->1]
        
        # If list has nothing, return nothing(Because there is nothing to reverse)
        if self.head == None:
            return

        # Best Case(When we reached end of our linked list having reversed a pointer)
        # Reached the tail and change that tail's pointer points previous element, not points 'None'
        elif current.next == None: # Reach the tail
            self.tail = self.head # Set the tail as previous head ! (Set the `5`(which was tail) as `Head`(which is previous head))
            current.next = previous # Set the current node point previous node
            self.head = current # Set the current as 'New Head'
        
        # iterate through the list 
        else:  
            next = current.next
            current.next = previous
            self.reverse_list_recur(next,current)


# Test
my_list = LinkedList()
my_list.add_val(1)
my_list.add_val(2)
my_list.add_val(3)
my_list.add_val(4)
my_list.add_val(5)
print(my_list)
my_list.reverse_list_recur(my_list.head, None)
print(my_list)