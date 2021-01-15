# Lists, dicts, sets and tuples - Intro to compound data types in Python

#List 
node_1 = 'custom object'
my_data_type_list = [1, 2, False, "Robert", None, node_1, 5.0]
print(my_data_type_list)
print(type(my_data_type_list)) #<class 'list'>
print(my_data_type_list[3]) #Robert

# Dictionary (key-value pair)
my_data_type_dic = {
    1: "Hello",
    2: "Robert",
    3: None,
    4: node_1,
    5: 5.0
}
print(my_data_type_dic)
print(type(my_data_type_dic)) #<class 'dict'>
# To access the `value` in dictionary, we have to use 'Key' instead of 'Index'
print(my_data_type_dic[2]) #Robert

# Sets : It's very sisimlar to List but they use `{}` instead of `[]`
# Also big diffence between `Lists` and `Sets` is `Sets` does not allow to have duplicated data
# and Sets does not have ordering system. Every time run it, the sets element order is random
my_data_type_set = {1, 2, False, "Robert", None, node_1, 5.0, 1}
print(type(my_data_type_set))
print(my_data_type_set) # {False, 1, 2, 5.0, None, 'Robert', 'custom object'} only have one `1`

# Tuples: Very similar to Lists but tuple use () not [] also, A tuple is a collection which is ordered and unchangeable. Tuple items are ordered, unchangeable, and allow duplicate values.
my_data_type_tuple = (1, 2, False, "Robert", None, node_1, 5.0, 1)
print(type(my_data_type_tuple)) #<class 'tuple'
print(my_data_type_tuple)
print(my_data_type_tuple[6])
#my_data_type_tuple[4] = 'Python' # Error: TypeError: 'tuple' object does not support item assignment
print(my_data_type_tuple)
