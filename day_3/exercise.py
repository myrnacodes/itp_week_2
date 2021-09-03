# ITP Week 2 Day 3 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
#     - A function that multiplies three integers
#     - A function that adds four integers

def sub(num1, num2):
    return num1-num2

def mult_three_nums(num1, num2, num3):
    return num1 * num2 * num3

def add_four_nums(num1, num2, num3, num4):
    sum = num1 + num2 + num3 + num4
    return sum

# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.

def calculator():
    first_number = float(int(input("first number:"))
    type_of_operation = input("please choose: +, -, *, /: ")
    second_number = float(input("second number: "))
    return sum

# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.  You may use the math module from the Python standard library.


