# Set the BST's Node data format
from datetime import datetime, timedelta

class Node:

    # Assign time as a Node
    def __init__(self,key):

        # Split the imported data format from txt file. 
        sched_time, duration, name_of_job = key.split(",")
        raw_sched_time = datetime.strptime(sched_time, '%H:%M')
        key = raw_sched_time.time()
        end_time = (raw_sched_time + timedelta(minutes=int(duaration))).time()
        
        # Design a Node
        self.data = key
        self.scheduled_end = end_time
        self.duration = duration
        self.name_of_job = name_of_job.rstrip()
        self.left_child = None
        self.right_child = None

        def __str__(self):
            return f"Time: {self.data}, Duration: {self.duration}, End: {self.scheduled_end}, Job Name: {self.name_of_job}"

