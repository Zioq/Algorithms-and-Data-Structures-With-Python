''' Try to remove parents  who has one child'''

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
            # If we want to delete root node which has a childe node, we have to add new condition.
        
            if key == curr.data:
                # We need to test for how many children current node trying to delete actually has.
                if curr.left_child == None and curr.right_child == None:
                # This particular condition work when there is children node .(When you want to delete leaf node)
                    # Remove the link from the prev(parent) node
                    if is_left:
                        prev.left_child = None
                    else:
                        prev.right_child = None
                
                elif curr.left_child == None: # When we add F, G and delete F 
                    # Check for existing previous node
                    if prev:
                        # check for if the current is left_child of previous or not
                        if is_left:
                            # current is left child of previous node 
                            prev.left_child = curr.right_child
                        else:
                            prev.right_child = curr.right_child
                    # if there is no previous, which means root
                    else:
                        # Make a F as root node
                        self.root = curr.right_child

                elif curr.right_child == None: # When we add F, C and delete F 
                    # Check for existing previous node
                    if prev:
                        # check for if the current is left_child of previous or not
                        if is_left:
                            prev.left_child = curr.left_child;
                        else:
                            prev.right_child = curr.left_child; 
                    
                    # if there is no previous, which means root
                    else:
                        self.root = curr.left_child

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
