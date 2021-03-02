# Build a Binary Search Tree 

class Node:
    
    def __init__(self,key):
        # Set the Node (data, left_child, right_child)
        self.data = key
        self.left_child = None
        self.right_child = None

class BSTDemo:

    def __init__(self):
        # initialize Root Node
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root,key)

    # use underscore(_) in fornt of method name to imply private method in ptyon.
    def _insert(self, curr, key):
        if key.data > curr.data:
            if curr.right_child == None:
                curr.right_child = key
            else:
                self._insert(curr.right_child,key)
        elif key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child,key)


tree = BSTDemo()
tree.insert("F")
print(tree.root.data)
tree.insert("C")
print(tree.root.left_child.data)
tree.insert("G")
print(tree.root.right_child.data)
tree.insert("A")
print(tree.root.left_child.left_child.data)
tree.insert("B")
print(tree.root.left_child.left_child.right_child.data)
tree.insert("K")
print(tree.root.right_child.right_child.data)
tree.insert("H")
print(tree.root.right_child.right_child.left_child.data)