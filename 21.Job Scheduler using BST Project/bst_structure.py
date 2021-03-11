# Set the BST's Node data format
from datetime import datetime, timedelta

class Node:

    # Assign time as a Node
    def __init__(self,key):

        # Split the imported data format from txt file. 
        sched_time, duration, job = key.split(",")
        raw_sched_time = datetime.strptime(sched_time, '%H:%M')
        key = raw_sched_time.time()
        end_time = (raw_sched_time + timedelta(minutes=int(duration))).time()
        
        # Design a Node
        self.data = key
        self.scheduled_end = end_time
        self.duration = duration
        self.job = job.rstrip()
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"Time: {self.data}, Duration: {self.duration}, End: {self.scheduled_end}, Job: {self.job}"

class BSTDemo:
    
    def __init__(self):
        self.root = None

    def insert(self,key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
            self.print_out(key,True)
        else:
            self._insert(self.root,key)

    def _insert(self, curr, key):
        # Add new condtition that check new job's time is duplicated or not
        if key.data > curr.data and key.data >= curr.scheduled_end:
            if curr.right_child == None:
                curr.right_child = key
                self.print_out(key,True)
            else: 
                self._insert(curr.right_child, key)
        elif key.data < curr.data and key.data <= curr.scheduled_end:
            if curr.left_child == None:
                curr.left_child = key
                self.print_out(key,True)
            else:
                self._insert(curr.left_child, key)
        else:
            self.print_out(key,False)

    # Method to print out result
    def print_out(self,key, success):
        if success:
            print(f"Added:\t\t {key.job}")
            print(f"Begin:\t\t {key.data}")
            print(f"End:\t\t {key.scheduled_end}")
            print("-"*60)

        else:
            print(f"Failed to add a job:\t\t {key.job}")
            print(f"Begin:\t\t {key.data}")
            print(f"End:\t\t {key.scheduled_end}")
            print(f"Error:\t\t Time slot overlap, please verify")
            print("-"*60)

    def in_order(self):
        print("Today job schedule")
        print("-"*60)
        self._in_order(self.root)
        print("-"*60)
    
    def _in_order(self,curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr)
            self._in_order(curr.right_child)

    def find_val(self,key):
        return self._find_val(self.root, key)

    def _find_val(self,curr,key):
        if curr:
            if curr.data == key:
                return curr
            elif curr.data > key:
                self._find_val(curr.right_child,key)
            else:
                self._find_val(curr.left_child,key)

    def min_right_subtree(self, curr):
        if curr.left_child == None:
            return curr
        else:
            return self.min_right_subtree(curr.left_child)

    def delete_val(self,key):
        self._delete_val(self.root, None, None, key)

    def _delete_val(self,curr, prev, is_left, key):
        if curr:
            if key == curr.data:
                if curr.left_child and curr.right_child:
                    min_child = self.min_right_subtree(curr.right_child)
                    curr.data = min_child.data
                    self._delete_val(curr.right_child, curr, False, min_child.data)

                elif curr.left_child == None and curr.right_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = None
                        else:
                            prev.right_child = None
                    else:
                        self.root = None
                # F, G and delete F 
                elif curr.left_child == None:
                    if prev:
                        # C,A,B and delete A 
                        if is_left:
                            prev.left_child = curr.right_child
                        else:
                            prev.right_child = curr.right_child
                    else:
                        self.root = curr.right_child
                
                # curr.right_child == None
                # F,C and delete F 
                else:
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

    # Method to check a length of tree. This will be used to add new job
    def lenght_of_schedule(self):
        return _length_of_schdule(self.root)

    def _length_of_schdule(self,curr):
        if curr is None:
            return 0
        else:
            1 + self._length_of_schdule(curr.left_child) + self._length_of_schdule(curr.right_child)
''' 
# Test
data_tree = BSTDemo()
#data_tree.insert("4:30,30,Price Loader")
data_tree.insert("4:30,30,Price Loader")
data_tree.insert("3:00,15,Load Transactions")
data_tree.insert("8:30,90,Balance Sheet")
data_tree.insert("1:30,60,Web Refresh")
data_tree.insert("15:00,20,Transaction Validator")
data_tree.insert("18:00,75,Batch Process")
data_tree.in_order()
start_time = "18:00"
key_to_find = datetime.strptime(start_time, '%H:%M').time()
data_tree.delete_val(key_to_find)
data_tree.in_order() '''