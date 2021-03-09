''' 
The thing we should know about algorithm when we want to delete leaf node. 
We need to remove a "link from the parent" 
1) We need to know previous(parents) node of what we wnat to delete.
2) we need to know which child(left_child or right_child) we want to delete
'''

class Node:
    def __init__(self, key):
        self.data = key
        self.right_child = None
        self.left_child = None


class BSTDemo:

    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root, key)

    def _insert(self, curr, key):
        if curr.data < key.data:
            if curr.right_child == None:
                curr.right_child = key
            else:
                self._insert(curr.right_child, key)
        elif curr.data > key.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child, key)

    def in_order(self):
        self._in_order(self.root)
        print("")

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr.data, end=" ")
            self._in_order(curr.right_child)

    def delete_val(self, key):
        self._delete_val(self.root, None, None, key)

    def _delete_val(self, curr, prev, is_left, key):
        if curr:
            if key == curr.data:
                #self.root = None
                # Remove the link from the prev(parent) node
                if is_left:
                    prev.left_child = None
                else:
                    prev.right_child = None
            elif key < curr.data:
                self._delete_val(curr.left_child, curr, True, key)
            elif key > curr.data:
                self._delete_val(curr.right_child,curr, False, key)
        else:
            print(f"{key} not found in Tree")


tree = BSTDemo()
tree.insert("F")
tree.insert("G")
tree.in_order()
tree.delete_val("G")
tree.in_order()
