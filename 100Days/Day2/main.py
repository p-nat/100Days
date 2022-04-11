num_char = len(input("What is your name? \n"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = 123
print(type(a))  # Prints and checks data type - which is an int.

a = str(123)  # Prints and converts data type to a str.
print(type(a))

a = float(123)  # Converts to a float.
print(type(a))

print(70 + float("100.5"))  # This will print int AND float.
print(str(70) + str(100))   # This will print the two strings together.


#
# Day 2, Exercise 1
#
## Cannot change the code below.
two_digit_number = input("Type a two digit number: ")
## Cannot change the code above.

# So find the data type, eg. string, interval, float.
(type(two_digit_number))

# Pull out the numbers with subscripting.
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

# Turn variables into int and + them together.
result = int(first_digit) + int(second_digit)

# Print the result.
print(result)


3 + 5
7 - 2
3 * 2
6 / 3  # When you device, you always end up with a float.
2 ** 2 # To the power of 2. Squared.
PEMDAS-LR # Order of priority of operations, left to right.
()
**
* /
+ -
print(3 * 3 + 3 / 3 - 3)  # This order matters. Use thonny to see the order.

#
# Day 2, Exercise 2 (BMI Calculator)
#
# Cannot change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# # Cannot change the code above
# print(type(height))
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)

# Rounding numbers - 9 devided by 3, 2 decimals places
print(round(9 / 3, 2))
print(9 // 2) # Using // turns this float into an int.

result = 4 / 2 # 4 / 2 = 2, result is 2.
results /=2 # getting the result and device by 2.
print(result) # dev

