#Introduction to branching (if, elif, else) and conditionals
""" 
if condition:
    excute some code
elif condition:
    execute some other code
else:
    execute some ohter code """

print("Welcome to the calc program")
print("-"*30)
choice = input("Choose '1' to multiply, '2' to divide-> ")


if (choice == "1" or choice== "2"):
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    if (choice == "1"):
        print(f"{num_1} multiply by {num_2} is: {num_1 * num_2}")
    else:
        print(f"{num_1} devided by {num_2} is {num_1 / num_2}")
else:
    print("You've mand an invalid selection")

    