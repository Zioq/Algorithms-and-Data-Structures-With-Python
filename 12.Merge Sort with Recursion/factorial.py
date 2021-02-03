# Recursion mini-project 2 - Factorial
''' 
Factorial
- The product of an integer n , and all the integers below it.
- Factorial of 4 = 4 * 3 * 2 * 1 = 24 
- It's denoted by the ! after the number, so 5 factorial would be written as 5!
- Factorial 0 is 1
- Base case: 
    If ased for the factorial of 0, return 1 since 0! = 1 

Recursive build
1! = 1
2! = 2 * 1!
3! = 3 * 2!
4! = 4 * 3!
5! = 5 * 4!
...
n! = n * (n-1)! 
for n > 0

factorial(1) = 1
factorial(2) = 2 * factorial(1)
factorial(3) = 3 * factorial(2)
factorial(4) = 4 * factorial(3)
factorial(5) = 5 * factorial(4)  

'''

def factorial_recur(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recur(n-1)

z = 0 # expecting 1
print(f"The value of {z}! is {factorial_recur(z)}")
z = 1 # expecting 1
print(f"The value of {z}! is {factorial_recur(z)}")
z = 5 # expecting 120
print(f"The value of {z}! is {factorial_recur(z)}")