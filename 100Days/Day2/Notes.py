# Print - Prints a string into the console.
print("Hello There")

# input prompt for the user
input("What is your name? ")

# Variables give a name to a piece of data, like a box with a label. Notice a str needs "" and an int doesnt.
my_age = 12
my_name = "NatYolo"

# The += Operator - This is a convenient way of saying: take the previous value and add to it.
my_age = 12
my_age += 4
# my age is now 16.

# is***()  is the function giving boolean output. In the example, isupper() function will check the value of the
# variable "my_name" whether is written in Upper cases and return with "yes" or "no" as an output.

print(my_name.isupper())

# len()  Counts the number of characters in the string.
print(len(input("What is your name? ")))
# .index() will find the index of the sting inside the variable.the index start from "0"
# .replace("value you want to replace","value you want to replace with") >> will find the value or parameter
# .replace("V1","V2") >> will find "V1" in the variable and replace "V2" in the variable.

# To add a paragraph break, a new paragraph put in \n
print("Hello World\nHello World")

#
# Data Types
#
# Strings - "Hey" or "123" with double quotes.
print("Hello")

# Integer - Whole numbers without decimal places.
print(123)
print(123 + 456)

# Float - Floating point number, decimal number.
print(3.14159)

# Boolean - Two values, either True or False.
True
False

# Subscript - pulling out a number from a string.
print("Hello"[0])

# Checking Data Types
age = 23
type(age) # This will print out the type of a variable: <class 'int'>

#  Converting Data Types
float()
int()
str()

#
