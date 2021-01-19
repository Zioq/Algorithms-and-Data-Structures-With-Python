# Dictionaries, sets and tuples

''' 
1. Dictionary 
- Dictionaries are used to store data values in key:value pairs.
- A dictionary is a collection which is unordered, changeable and does not allow duplicates.
- Dictionaries are written with curly brackets, and have keys and values
'''

my_dictionary = {'name': 'Robert', 'course': 'python', 'fav_food': 'pizze'}

phone_dic = {'Robert': '111-111-1111',
             'Shawn': '333-333-3333',
             'Tomo': '222-222-2222'}

word_dict = {
    'a':
    {
        'apple': 'the round fruit of a tree of the rose family',
        'ant': 'an insect which cleans up the floor'
    },
    'b':
    {
        'bad': 'of poor quality or low standard',
        'buisness': 'season 8 of GOT'
    }
}

# Get the value associated with key
print(word_dict['a'])

# Get the values nested in uppper value
print(word_dict['b']['bad'])

# Combine the value
print(word_dict['a']['apple'], word_dict['b']['bad'])
print(word_dict['a']['apple'], word_dict['b'])

# use a dictionary method .get()
# If the key doesn't exists in dictionary, return `None` 
print(my_dictionary.get('name'))
print(my_dictionary.get('job')) # None

# To add a new key-value set
my_dictionary['job'] = 'python programmer'
print(my_dictionary.get('job')) # Now return `python programmer`

# Change value of key 
my_dictionary['course'] = 'java'
print(my_dictionary) #{'name': 'Robert', 'course': 'java', 'fav_food': 'pizze', 'job': 'python programmer'}

# Get all keys in the dictionary -> `.keys()`
print(my_dictionary.keys()) # dict_keys(['name', 'course', 'fav_food', 'job'])

# Get all values in the dictionary -> `values()`
print(my_dictionary.values()) # dict_values(['Robert', 'java', 'pizze', 'python programmer'])

# Get all key-value pairs in dictionary -> `items()` 
# returns dictioanry data as `tuple` format

print(my_dictionary.items()) # dict_items([('name', 'Robert'), ('course', 'java'), ('fav_food', 'pizze'), ('job', 'python programmer')]) 

for k,v in my_dictionary.items():
    print(k, v)