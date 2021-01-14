#Print formatting and special characters

stock_price = "1100"
print("Today's price for google stock is:", stock_price)
print("Today's price for google stock is: {}".format(stock_price))

# f-string syntax: python3.6 uppper version
#print(f"Today's price for google sotck is: {stock_price}")

today_price = "1100"
yesterday_price = "1000"
print("Today's price: {}, Yesterday's price: {}".format(today_price,yesterday_price))
print(f"Today's price: {today_price}, yesterdya's price: {yesterday_price}")

#Special characters
# \ - is an excape character, it excapes the special character
#following it in a string
# \n - species new line within the string
# \t - adds a tab in it's place within the string 

print("My name is jon snow and \
not only do I know nothing but \
I also do nothing ")

print("My name is jon snow\nI know nothing\nI also do nothing")

print("My name is jon snow\n \tI know nothing\n \t\tI also do nothing")

print("I'm using the \\n special character to create new lines")