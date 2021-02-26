class Node:

    def __init__(self, data=None):
        # Set the data
        self.data = data
        # Set the pointer
        self.next = None

    def __str__(self):
        return f"{self.data}"


class LinkedList:

    # Initialize linked list(At the beginning, the linked list has Head with None, and Tail with None)
    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        ''' Add x to the end of the list '''
        if not isinstance(x, Node):
            x = Node(x)
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def __str__(self):
        # [5->4->10->1]
        to_print = ""
        current = self.head
        while current is not None:
            to_print = to_print + str(current.data) + "->"
            current = current.next
        if to_print:
            return "["+ to_print[:-2] +"]"
        return "[]"


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

my_list = LinkedList()

my_list.append_val(node1)
my_list.append_val(node2)
my_list.append_val(node3)
my_list.append_val(node4)
my_list.append_val(node5)
print(my_list)

my_list_2 = LinkedList()
node_2_1 = Node(5)
node_2_2 = Node(4)
node_2_3 = 10
node_2_4 = 1
my_list_2.append_val(node_2_1)
my_list_2.append_val(node_2_2)
my_list_2.append_val(node_2_3)
my_list_2.append_val(node_2_4)
print(my_list_2)
