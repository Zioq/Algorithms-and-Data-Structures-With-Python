# Build a Binary Search Tree

class Node:

    def __init__(self, key):
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
            self._insert(self.root, key)

    # use underscore(_) in fornt of method name to imply private method in python.
    def _insert(self, curr, key):
        if key.data > curr.data:
            if curr.right_child == None:
                curr.right_child = key
            else:
                self._insert(curr.right_child, key)
        elif key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child, key)

    def in_order(self):
        """ Algorithm in-order 
        1. Traverse the left sub-tree
        2. Visit the root
        3. Traverse the right sub-tree
        """
        self._in_order(self.root)
        print("")

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr.data, end=" ")
            self._in_order(curr.right_child)

    def pre_order(self):
        """ Algorithm in-order 
        1. Visit the root
        2. Traverse the left sub-tree
        3. Traverse the right sub-tree
        """
        self._pre_order(self.root)
        print("")

    def _pre_order(self, curr):
        if curr:
            print(curr.data, end=" ")
            self._pre_order(curr.left_child)
            self._pre_order(curr.right_child)

    def post_order(self):
        """ Algorithm in-order 
        1. Traverse the left sub-tree
        2. Traverse the right sub-tree
        3. Visit the root
        """
        self._post_order(self.root)
        print("")

    def _post_order(self, curr):
        if curr:
            self._post_order(curr.left_child)
            self._post_order(curr.right_child)
            print(curr.data, end=" ")

    def find_val(self, key):
        return self._find_val(self.root, key)

    def _find_val(self, curr, key):
        if curr:
            if key == curr.data:
                return "Value found in tree"
            elif key < curr.data:
                return self._find_val(curr.left_child, key)
            else:
                return self._find_val(curr.right_child, key)
        return "Value not found in tree"

    
    def delete_val(self, key):
        self._delete_val(self.root, None, None, key)
    
    # Delete leaf node 
    def _delete_val(self, curr, prev, is_left, key):
        if curr:
            if key == curr.data:
                print("Node is deleted")
                # Delete node by assigning `None`
                if is_left:
                    prev.left_child = None
                else:
                    prev.right_child = None

            elif key < curr.data:
                print("Found node to delete on left side of node")
                self._delete_val(curr.left_child, curr, True, key)

            elif key > curr.data:
                print("Found node to delete on right side of node")
                self._delete_val(curr.right_child, curr, False, key)
        else:
            print(f"{key} not found in Tree")


""" 
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
"""

#tree = BSTDemo()
# tree.insert("H")
# tree.insert("D")
# tree.insert("I")
# tree.insert("M")
# tree.insert("J")
# tree.insert("L")
# tree.insert("F")
# tree.insert("C")
# tree.insert("G")
# tree.insert("A")
# tree.insert("B")
# tree.insert("K")
# tree.insert("E")
# tree.in_order()
# tree.pre_order()
# tree.post_order()
# print(tree.find_val("E")) # Value found in tree
# print(tree.find_val("Z")) # Value not found in tree

tree = BSTDemo()
tree.insert("F")
tree.insert("G")
tree.in_order()
tree.delete_val("G")
tree.in_order()
