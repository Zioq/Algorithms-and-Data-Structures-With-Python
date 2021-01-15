# Building if, elif, else blocks incrementally
# Branching and control flow step by step


#Python's true/false condtion is should be start with upper-capital.(True/False) not (true/false)
truth_condition = True

if truth_condition:
    print("Turth")

choice = '2'

if choice == '1':
    print("You have chosen option 1")
elif choice == '2':
    print("You have chosen option 2")
else:
    print("You have mad an invalid choice")

""" [Conditional Statement]
True and True -> True
True and False -> False
True or True -> True
True or False -> False  """

made_payment = True
a = "Please pay montly premium"
b = "Welcome to your homepage"

if not made_payment:
    print(a)
else:
    print(b)

i = 5
j = 10
k = 30

# if the condtion true, execute code, THEN EXIT THE WHOLE BRANCH
if i < j and i<k:
    print("i is less than j and k")
elif i == j and i ==k:
    print("i is eqaul to j and k")
elif i == j or i ==k:
    print("i is equal to either j or k")
else:
    print("something else")

# One-line if condition
course = 'Python'
a = 'enrolled in python course'
b = 'enrolled in some other course'
""" 
if course == 'Python':
    print(a)
else: 
    print(b)
"""
print(a) if course == 'Python' else print(b)