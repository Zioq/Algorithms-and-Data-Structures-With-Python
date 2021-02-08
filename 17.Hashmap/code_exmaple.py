records = [('robert@gmail.com', 'Hello World'),
           ('shawn@gmail.com', 'Hello to you too'), 
           ('jenna@gmail.com', 'I love python')]

for index, record in enumerate(records):
    key,value = record
    if key == "shawn@gmail.com":
        break

print(records[index])
