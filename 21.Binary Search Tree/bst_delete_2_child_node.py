''' Try to remove parents who has two child

Delete taget: C,F or K 
            F
          /   \
         C     G      
       /   \     \
      A     E     K
                /   \
               H     M 

1) If we decide to delete `F`, then look at right subtree and find min value, which is G
2) If we found G, copy the data from the G to my current data(which is F)
            G
          /   \
         C     G      
       /   \     \
      A     E     K
                /   \
               H     M 

3) Then, call delete function again to delete G(not copeid one, the original one)
3-1) Make G's parent point to G's child
3-2) And simply remove the G, by making G's right child point to None
            G
          /   \
        C       K      
       / \     / \
      A   E   H   M 
                 
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

    # Add new method which found min value in right sub tree. curr means `right-sub-tree`
    def min_right_subtree(self, curr):
        if curr.left_child == None:
            return curr
        else:
            # call recursvie function till found min value in `right-sub-tree`
            return self.min_right_subtree(curr.left_child)

    def delete_val(self, key):
        self._delete_val(self.root, None, None, key)

    def _delete_val(self, curr, prev, is_left, key):
        if curr:
            # If we want to delete root node which has a childe node, we have to add new condition.
            if key == curr.data:
                # We need to test for how man children current node tring to delete actually has 2 children.
                if curr.left_child and curr.right_child:
                    min_child = self.min_right_subtree(curr.right_child)
                    curr.data = min_child.data
                    self._delete_val(curr.right_child, curr, False, min_child.data)

                # We need to test for how many children current node trying to delete actually has.
                elif curr.left_child == None and curr.right_child == None:
                    if prev:
                    # This particular condition work when there is children node .(When you want to delete leaf node)
                        # Remove the link from the prev(parent) node
                        if is_left:
                            prev.left_child = None
                        else:
                            prev.right_child = None
                    else:
                        self.root = None

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

                else: # When we add F, C and delete F 
                    # Check for existing previous node
                    if prev:
                        # check for if the current is left_child of previous or not
                        if is_left:
                            prev.left_child = curr.left_child
                        else:
                            prev.right_child = curr.left_child
                    
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
tree.insert("C")
print("Test deleting leaf node which is left child of parent")
tree.in_order()
tree.delete_val("C")
tree.in_order()
tree.insert("G")
print("Test deleting leaf node which is right child of parent")
tree.in_order()
tree.delete_val("G")
tree.in_order()
tree.insert("A")
print("Test deleting parent/root node which has one child")
tree.in_order()
tree.delete_val("F")
tree.in_order()
print("Test deleting root node which has no children")
tree.in_order()
tree.delete_val("A")
tree.in_order()
tree.insert("F")
tree.insert("C")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("E")
tree.insert("H")
tree.insert("D")
tree.insert("I")
tree.insert("M")
tree.insert("J")
tree.insert("L")
tree.in_order()
tree.delete_val("F")
tree.in_order()
tree.in_order()
tree.delete_val("K")
tree.in_order()
tree.in_order()
tree.delete_val("C")
tree.in_order()
tree.delete_val("Z")