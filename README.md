# python-

# ASSIGNMENT 1

Task-1
"""
Problem Statement: Write a Python program that does the following:

1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
    o Addition
    o Subtraction
    o Multiplication
    o Division
3.  Displays the results of each operation on the screen.

"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 \* num2
division = num1 / num2

print("Addition : ", addition)
print("Subtraction : ", subtraction)
print("Multiplication : ", multiplication)
print("Division : ", division)

Task-2

""" "
Problem Statement: Write a Python program that:

1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.

"""

first_name = input("Enter the first name : ")
last_name = input("Enter the last name : ")

greeting = "Hello, " + first_name + " " + last_name + "! Welcome to the Python program."

print(greeting)

# ASSIGNMENT 2

Task-1 :
"""
Problem Statement: Write a Python program that:

1. Takes an integer input from the user.
2. Checks whether the number is even or odd using an if-else statement.
3. Displays the result accordingly.
   """
   num = int(input("Enter the number: "))

if num%2 == 0:
print(f"{num} is an even number")
else:
print(f"{num} is an odd number")

Task-2 :
"""
Problem Statement: Write a Python program that:

1.  Uses a for loop to iterate over numbers from 1 to 50.
2.  Calculates the sum of all integers in this range.
3.  Displays the final sum.
    """
    
total_sum = 0

for num in range(1, 51):
total_sum += num

print("The sum of numbers from 1 to 50 is:", total_sum)
