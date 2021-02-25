# Application usage
''' 
- In application you will have to load data from persistent memory to working memory as objects.
- Once loaded, you can work with data in these objects and perform operations as necessary

Exmaple)
1. In Database or other data source
2. Load data
3. Save it in data structure like `Dictionary`
4. Get the data from the data structure and work with process data as necessary
5. Produce output like presentation or update data and upload to the Database etc

In this project we follow those steps like this
1. Text file - email address and quotes
2. Load data
3. Populate the AlgoHashTable
4. Search for quotes from specific users
5. Present the data to the console output
'''

# Eamil address and quotes key-value data generator
from random import choice
from string import ascii_lowercase as letters

list_of_domains = ['yaexample.com','goexample.com','example.com']

quotes = [  'Luck is what happens when preparation meets opportunity',
            'All cruelty springs from weakness',
            'Begin at once to live, and count each separate day as a separate life',
            'Throw me to the wolves and I will return leading the pack']

def generate_name(lenght_of_name):
    return ''.join(choice(letters) for i in range(lenght_of_name))

def get_domain(list_of_domains):
    return choice(list_of_domains)

def get_quotes(list_of_quotes):
    return choice(list_of_quotes)

def generate_records(length_of_name, list_of_domains, total_records, list_of_quotes):
    with open("data.txt", "w") as to_write:
        for num in range(total_records):
            key = generate_name(length_of_name)+"@"+get_domain(list_of_domains)
            value = get_quotes(quotes)
            to_write.write(key + ":" + value + "\n")
        to_write.write("mashrur@example.com:Don't let me leave Murph\n")
        to_write.write("evgeny@example.com:All I do is win win win no matter what!\n")

generate_records(10, list_of_domains, 100000, quotes)
