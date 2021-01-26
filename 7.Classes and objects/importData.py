# function to convert string to parameters for __init__
# function to covert Student object to string for write fo file
# special function - equality test


file_name = "data.txt"

""" # Open file
f = open(file_name)

# Read whole text data
f_content = f.read()
print(f_content)

# Read line by line
for line in f:
    print(line.strip())

# Close file
f.close() """

def prep_record(line):
    line = line.split(":")
    first_name, last_name = line[0].split(",")
    course_details = line[1].rstrip().split(",")
    return first_name, last_name, course_details


def prep_to_write(first_name,last_name, courses):
    full_name = first_name +','+ last_name
    courses = ",".join(courses)
    return full_name+":"courses


# Context Manager
with open(file_name) as f:
    for line in f:
        #print(line.strip())
        first_name,last_name,course_details = prep_record(line)
        print(first_name,last_name,course_details)


# Write content
record_to_add = "new,data:python,ruby,java"

# "w" means rewrite wtih content (delete it existsed data in the txt file), "a+" means append new data in the txt file
""" with open(file_name, "a+") as to_write:
    to_write.write(record_to_add+"\n") """


""" robert,han:python,rubpy,javascript
john,smith:java,c++,c
shawn,kim:go,ruby,javascriptnew,data:python,ruby,java
new,data:python,ruby,java """
