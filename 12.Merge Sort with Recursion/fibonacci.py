#Recursion mini-project 3 - Fibonacci series
''' 
Fibonacci Series
- It's a series of integers
- Value of the nth integer can be found by adding the values of the two previous integers in the series
- The series starts off with 0, 1, 1, 2, 3, 5, 8, 13

Base case
- If n = 0, return 0
- If n = 1, return 1

Rest of the series
n   fib(n)
0   0       
1   1        
2   1       fib(2) = 1 + 0 -> fib(1) + fib(0)
3   2       fib(3) = 1 + 1 -> fib(2) + fib(1)  
4   3       fib(4) = 2 + 1 -> fib(3) + fib(2)
5   5       fib(5) = 3 + 2 -> fib(4) + fib(3)
6   8       fib(6) = 5 + 3 -> fib(5) + fib(4)
7   13
8   21      
...         fib(n) = fib(n-1) + fib(n-2)


'''

def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

def fib_runner(z):
    print(f"The {z}th number in the fibonacci sequence is {fib_recur(z)}")

z = 0
fib_runner(z)
z = 1 
fib_runner(z)
z = 10
fib_runner(z)