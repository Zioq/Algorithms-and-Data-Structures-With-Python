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
            return f"Time: {self.data}, Duration: {self.duration}, End: {self.scheduled_end}, Job Name: {self.job}"

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
            pass

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

# Test
data_tree = BSTDemo()
#data_tree.insert("4:30,30,Price Loader")
data_tree.insert("4:30,20,Test")