# Methods and functions we can use on string objects
# len(), type(), id()
# capitalize(), upper(), lower(), strip(), find()
# split(), join()
# import string
# https://docs.python.org/3/library/

greeting = 'hello'
user = "robert"
message = "Welcome to the Algorithms course"
print(greeting, user, message)

#print string's lenght
print(len(greeting))
print(len(message)) # include space 

#print type
print(type(user)) # <class 'str'>
print(type(5)) # <class 'int'>

#print memory location of object -> id()
# Everything in python is an object (String, Number...)
print(id(greeting))
print(id(user))
print(id(message))

#capitalize() -> method returns a string where the first character is upper case.
print(greeting, user.capitalize(), message)
#print(dir(user)) #dir(string)->show all built-in method related to string

#upper() -> method returns a string where all characters are in upper case
#lower() -> method returns a string where all characters are in lower case
print(greeting.upper(), user.capitalize(), message.lower())

#strip() -> method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

txt1 = ",,,,,rrttgg.....banana....rrr"
x2 = txt.strip(",.grt")
print(x2)

#find() ->  method finds the first occurrence of the specified value. / method returns -1 if the value is not found.
print(message.find("course"))
print(message.find('z'))

#split() -> method splits a string into a list. You can specify the separator, default separator is any whitespace.
print(message.split())
message1 = "Welcome-to-the-Algorithms-course"
print(message1.split('-'))

#join() -> method takes all items in an iterable and joins them into one string. A string must be specified as the separator.
my_language = ['Python', 'JavaScript', 'Ruby']
print(" ".join(my_language))
print("-".join(my_language))

#import string medule
# import string
from string import ascii_lowercase #import sepcific medule
print(ascii_lowercase)