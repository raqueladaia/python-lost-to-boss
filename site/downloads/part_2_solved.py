###################################################################
# Welcome to Part 2!
###################################################################
# © 2024–2026 Raquel Adaia Sandoval Ortega · Python: From Lost to Boss I · https://sandovalortega.com/python-lost-to-boss-1/
# Free to reuse with credit: code under the MIT licence, course text under CC BY 4.0 (see LICENSE.txt).
# In this part we will learn about data types in Python.

# Anything after a "#" is a comment and will not be executed by Python.

############################################
# Integers and floats
############################################

x = 9  # integer
y = 8.7  # float

# You can create a breakpoint by clicking with the left mouse button 
# on the left side of the line number.
# Breakpoints need to be in a "readable" part of your code.
# Breakpoints next to comments or empty lines will not work.
# Set a breakpoint on the line below and run the code in debug mode.
# Python will only run the instructions before the breakpoint.
# But if any line has a syntax error (e.g. an unfinished `x =`), nothing runs at all:
# comment out the unfinished lines first.
print()

# You can convert floats into integers and vice versa
x = float(x)
y = int(y)

# Example: Create a float from an integer
x = float(3)
y = int(9.0534365213)

# If you don't know the type of a variable, you can use the type() function
print(type(x))

############################################
# Strings
############################################

# This is your first string
x = "Hello, World!"
print(x)

# You can also use single quotes to create strings
x = 'Hello, World!'
print(x)

# You can use triple quotes to create multi-line strings
x = """Hello,
World!"""
print(x)

# There are special characters (= escape sequence) that you can use in strings
# \n: newline
# \t: tab

x = "Hey!\nHow are you doing?"
print(x)

x = "Hey \t\t\t\tHow are you doing?"
print(x)

# To avoid the special characters (= escape sequences), you can use the r prefix
x = r"Hello, \nWorld!"
print(x)

# You can concatenate strings using the + operator
x = "Hello, "
y = "World!"
z = x + y
print(z)

# You can also multiply strings
x = "Hello! "
z = x * 3
print(z)

# You can convert integers and floats into strings
x = str(3)
y = str(3.1415)
# TODO: Compare the numbers that are strings with the numbers that are not strings
print(x == 3, y == 3.1415)  # False False: "3" is text, not the number 3
print(x == "3", y == "3.1415")  # True True: text compared with text

# You can convert strings into integers and floats
x = int("3")
y = float("3.1415")

# f-strings to format strings
x = 3
y = 3.1415
z = f"The integer is {x} and the float is {y}"
print(z)

# Outdated way to format strings, but you can still see it in circulating code
name = "Bob"
age = 30
message = "%s is %d years old." % (name, age)  # %s is a placeholder for a string and %d is a placeholder for an integer
print(message)

# You can access characters in a string using the [] operator
first_char = message[0]  # Python always starts counting from 0
second_char = message[1]
last_char = message[-1]  # You can also use negative numbers to access characters from the end of the string
second_to_last_char = message[-2]

# You can slice strings using the [] operator
first_three_chars = message[0:3]  # The first number is the starting index; the second is the ending index, which is NOT included ([0:3] gives 3 characters)
first_three_chars = message[:3]  # If you omit the starting index, it will start from the beginning
last_three_chars = message[-3:]  # If you omit the ending index, it will go until the end
first_five_chars = message[:5]

# You can change the case of a string .upper(), .lower(), .title(), .capitalize()
# Test all these methods and see what they do (e.g. message.upper())
print(message.upper())  # BOB IS 30 YEARS OLD.
print(message.lower())  # bob is 30 years old.
print(message.title())  # Bob Is 30 Years Old. (every word starts with a capital letter)
print(message.capitalize())  # Bob is 30 years old. (only the first letter is a capital)


############################################
# Booleans
############################################

x = True
y = False

# You can convert booleans into integers
x = int(True)
y = int(False)

# You can invert booleans
x1 = not True
x2 = not False

# You can generate a boolean by comparing two values
val1 = 100
val2 = 10
x1 = val1 == val2
x2 = val1 != val2
x3 = val1 > val2

# You can generate a boolean by combining two booleans with "and" and "or"
x_and = True and False
x_or = True or False

# You can combine multiple booleans with "and" and "or"
x = True
y = False
z = True
x_and = x and y and z

############################################
# Challenge 1:
# Create an integer from a float,
# include the integer in a string
# and print the resulting string
############################################
x = 3.4
y = int(x)
z = f"This is a float {x} and this, an integer: {y}"
print(z)

############################################
# Challenge 2:
# Write a five-line conversation
# (you need at least two characters,
# at least 5 lines,
# and at least 5 tabs)
############################################

# Define the characters
person_1 = "Bob"
person_2 = "Alice"

# Write the conversation and print it
conversation = f"{person_1}: Hey!\n\t{person_2}: Hi!\n\t\t{person_1}: How are you?\n\t{person_2}: I'm good, thanks!\n\t{person_1}: That's great!"
print(conversation)

############################################
# Challenge 3:
# Create 3 variables:
# one for your name, 
# one for the name of the course,
# one for the directory of your repository;
# and print a message with all three variables.
# Bonus: write \033[3m before the path and \033[0m after it, and print again.
############################################

# Create the 3 variables
name = "Your Name"
course = "Python: From Lost to Boss I"
repo = r"C:\Users\your_name\Documents\Repositories\lost_to_boss"

# Print the message
message = f"Hello,\nmy name is {name},\nI really enjoy {course} (obviously)\nand my repository is located here: {repo}"
print(message)

# Bonus: \033[3m switches italics on and \033[0m switches the formatting off again
message = f"Hello,\nmy name is {name},\nI really enjoy {course} (obviously)\nand my repository is located here: \033[3m{repo}\033[0m"
print(message)

# QUESTIONS:
# 1. What happened to the text when you used the \033[3m escape sequence?
#    (\033[0m switches the formatting back off)
# ADDITIONAL CHALLENGE:
# 1. Can you find the escape sequence to make the text bold?
print("\033[1mThis is bold\033[0m")  # \033[1m switches bold on, \033[0m switches it off

############################################
# Challenge 4:
# Create a variable that, based on
# two variables (age and has ID), will let me know
# if you can buy beer.
# Print all the variables in a string to let me know
# if you can buy beer and why.
############################################

# Variables to check if Bob can buy beer
age = 19
has_id = True

# New variable to check if Bob can buy beer
age_you_can_buy = 21

# Check if Bob can buy beer
permission_age = age >= age_you_can_buy
permission_full = permission_age and has_id

# Communicate the result
print(f'Bob is {age} and it is {has_id} that he has ID. Can Bob buy beer? {permission_full}')

###################################################################
# Additional challenges (these are optional but fun!)
###################################################################

# 1. Create a string and print it in reverse order
word = "Boss"
print(word[::-1])  # [start:end:step]: a step of -1 walks through the string backwards (ssoB)

# 2. Find the escape sequence to have the sign of mu (μ) in a string
print("The cell is 10 \u03bcm wide")  # \u03bc is the Unicode escape sequence for the Greek letter mu (μ)

###################################################################
# Congratulations on your first Python script! You finished Part 2!
###################################################################
