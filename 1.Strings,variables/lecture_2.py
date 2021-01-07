# concatenation, indexing, slicing, python console

# concatenation: Add strings each other

message = "The price of the stock is:"
price =  "$1110"
print(id(message))
#print(message + " " +price)
message = message + " " +price
print(id(message))

# Indexing
name = "interstella"
print(name[0]) #print i

# Slicing
# [0:5] first num is start point, second num is stop point +1, so it means 0~4 characters
print(name[0:5]) # print `inter` 
#[A:B:C] ->  A: Start point, B: Stop +1, C: Step size
nums ="0123456789"
print(nums[2:6]) # output: 2345
print(nums[0:6:2]) # output: 024
print(nums[::2]) # output : 02468
print(nums[::-1]) # -1 mena backward step so, it will reverse the array. output: 9876543210