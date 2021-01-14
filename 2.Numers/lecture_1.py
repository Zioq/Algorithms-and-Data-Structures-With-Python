# Numbers, math, type casting and input

# Numbers-Integers, floats
# 1. Math
# 2. Type Casting
# 3. Getting input from user

import math
#math.pow  -> return A float value, representing the value of x to the power of y (x^y)
print(math.pow(10,5)) #100000.0
print(math.pow(9, 3)) #729.0

#math.log() method returns the natural logarithm of a number, or the logarithm of number to base.
print(math.log2(1000000))

import random
print(random.randint(0,1000)) # generate random integer number between 0~1000

# Type casting
# Convert string to number(int/float)
num_1 = "10"
num_2 = "20"
result = num_1 + num_2
print(result)

convertToNum = int(num_1) + int(num_2)
print(convertToNum)

# Convert int into String
print(type(convertToNum))
convertToString = str(convertToNum)
print(type(convertToString))

#Getting input from user
print("Welcome to the multiplication program")
print("="*30)
number_1 = int(input("Enter a number to multiply~> "))
number_2 = int(input("Enter a second number to multiply~> "))
result = number_1 * number_2
print(result)