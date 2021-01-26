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

# Context Manager
with open(file_name) as f:
    for line in f:
        print(line.strip())

# Write content
record_to_add = "new,data:python,ruby,java"

# "w" means rewrite wtih content (delete it existsed data in the txt file), "a+" means append new data in the txt file
with open(file_name, "a+") as to_write:
    to_write.write(record_to_add+"\n")
