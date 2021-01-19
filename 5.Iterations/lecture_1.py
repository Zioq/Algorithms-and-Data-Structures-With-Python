# Iterators, for loops, generators, list comprehension

l = [6,8,1,4,10,7,9,2,5,4]
my_dic = {'py':'python','rb':'ruby','js':'javascript'}

# sum of all ints
sum = 0
for num in l:
    sum = sum + num

print(f"Sum using list: {sum}")

# range()
# range(10) ->range(0,10)
# list(lange(10)) -> [0,1,2,3,4,5,6,7,8,9]
print("Range(10): ", range(10))

for num in range(10):
    print(num)

print("")

for num in range(10):
    print(num,l[num])

print("")

for num in range(5):
    print(num,l[num])

print("")


sum = 0 
for num in range(len(l)):
    sum = sum + l[num]

print(f"Sum using range generator: {sum}")

run_times = int(input("How many times do you wnat to run? "))
for num in range(run_times):
    print(f"Run: {num+1}")

# Setting Range generator
print(list(range(0,10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,11))) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range,(1,20,2))) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
