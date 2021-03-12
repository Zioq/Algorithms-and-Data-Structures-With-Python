from datetime import datetime
from bst_structure import Node, BSTDemo

tree = BSTDemo()

# Open the txt tile
with open("data.txt") as f:
    for line in f:
        tree.insert(line)

# Method for adding a new job 
def add_new_job():
    start_time = input("Enter the time in hh:mm format, here is an exmaple, 18:00 or 6:30 ->")
    while True:
        try:
            datetime.strptime(start_time,'%H:%M')
        except ValueError:
            print("Incorrect time format, please enter this format ->  hh:mm  ex, 18:30, 6:30")
            start_time = input("Enter the time in hh:mm format, here is an exmaple, 18:00 or 6:30 ->")
        else:
            break
        
    duration = input("Enter the duration time of job in minutes, ex 60 ->")
    while True:
        try:
            int(duration)
        except ValueError:
            print("Please enter a number for number of minutes")
            duration = input("Enter the duration time of job in minutes, ex 60 ->")
        else:
            break
    
    job = input("Enter the name of the job (case sensitive)-> ")
    
    return start_time, duration, job

while True:
    print("Please enter the number to execute program")
    print("Press 1 to view today's scheduled jobs")
    print("Press 2 to add a job to today's schedule")
    print("Press 3 to delete a job from the schedule")
    print("Press 4 to quit")

    choice = input("Enter your choice => ")
    try:
        entry = int(choice)
    except ValueError:
        print("please enter a number between 1 and 4")
        print("\n")
        continue
    
    if int(choice) == 1: 
        tree.in_order()

    elif int(choice) == 2:
        print("You chose `2` to add new job on the schedule")
        print("* Caution *")
        print("If your new job time slot is already occupied, you cannot add new job on that time slot.")
        start_time, duration, job = add_new_job()
        
        # Adpat to a proper format  
        new_line = start_time + "," + duration + "," +job
        
        # Check for previous lenght of tree
        prev_length = tree.length()
        
        # Insert new_line as a node
        tree.insert(new_line)
        
        # Adjust new data to txt file dynamically
        if prev_length == tree.length()-1:
            with open("data.txt", "a+") as to_write:
                to_write.write(new_line+"\n")
        input("Press any key to continue... ")



    elif int(choice)  == 3:
        print("You chose `3` to delete a job on the schedule")
        
        start_time, duration, job = add_new_job()
        key_to_find = datetime.strptime(start_time,'%H:%M').time()
        result = tree.find_val(key_to_find)
        if result:
            if result.job == job and result.duration == duration:
                print("Removing job's detail->")
                print(result)
                tree.delete_val(key_to_find)
                print("The job successfully removed")
                # Delete job in txt file too
                with open("data.txt", "r") as f:
                    lines = f.readlines()
                with open("data.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != start_time+","+duration+","+job:
                            f.write(line)
                input("Press any key to continue... ")
            else:
                print("The name and/or duration of job did not match, delete failed")
                input("Press any key to continue... ")
        else:
            print("Job not found")
            input("Press any key to continue... ")

    elif int(choice) == 4:
        print("Thank you :D bye!")
        break
    else:
        print("please enter a number between 1 and 4")
