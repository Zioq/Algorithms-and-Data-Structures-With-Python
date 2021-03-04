class Node:
    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None


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
        self._in_order(self.root)
        print("")

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr.data, end=" ")
            self._in_order(curr.right_child)

    def delete_val(self, key):
        self._delete_val(self.root, None, None, key)

    # Deleting nodes with 1 child node
    def _delete_val(self, curr, prev, is_left, key):
        if curr:
            if key == curr.data:
                if curr.left_child and curr.right_child:
                    print("problem scenario")
                if curr.left_child == None and curr.right_child == None:
                    if is_left:
                        prev.left_child = None
                    else:
                        prev.right_child = None

                elif curr.left_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.right_child
                        
                        else: 
                            prev.right_child = curr.right_child
                    else:
                        self.root = curr.right_child
                elif curr.right_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.left_child
                        
                        else: 
                            prev.right_child = curr.left_child
                    else:
                        self.root = curr.left_child

            elif key < curr.data:
                self._delete_val(curr.left_child, curr, True, key)
            
            elif key > curr.data:
                self._delete_val(curr.right_child, curr, False, key)

        else:
            print(f"{key} not found in Tree")


tree = BSTDemo()
tree.insert("F")
tree.insert("G")
tree.in_order()
tree.delete_val("F")
tree.in_order()
