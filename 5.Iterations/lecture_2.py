# Iterators, for loops, generators, list comprehension

l = [6,8,1,4,10,7,9,2,5,4]
my_dic = {'py':'python','rb':'ruby','js':'javascript'}


for item in my_dic:
    print(item) # only print `key`
 
print(my_dic.items()) #dict_items([('py', 'python'), ('rb', 'ruby'), ('js', 'javascript')]) -> trun into tuple 

for item in my_dic.items():
    print(item)
    ''' 
    ('py', 'python')
    ('rb', 'ruby')
    ('js', 'javascript') 
    '''

# We can unpack tuple. So if itme is tuple we can assign each of key / value in a new variable
# This way only allowed you when the dictionary is changed as tuple `.items()`
for item in my_dic.items():
    key, value = item
    print(f"Key is {key}, and Value is {value}")
print("")

print("Shorten way")
for key, value in my_dic.items():
    print(f"Key is {key}, and Value is {value}")