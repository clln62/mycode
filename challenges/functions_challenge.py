# Make a calculator that takes two integers and adds/subtracts/divides/multiplies them!
# Use FUNCTIONS to create a calculator! Your script must accept the following user input:

# a float/integer
# another float/integer
# an operator (add, subtract, divide, multiply)
# Your script should return the answer!

# BONUS 1: Make the script human-error proof. Use IF/ELIF/ELSE and TRY/EXCEPT where necessary!

# BONUS 2: If the user types in a bad input, have them type it in again! Use a WHILE LOOP!

num1 = 0.0
num2 = 0.0
total = 0.0
symbol = ""


def add (a, b):
    global total
    total += a + b
    print(total)

def subtract (a, b):
    print(a - b)

def multiply (a, b):
    print(a * b)

def divide (a , b):
    print(a / b)


def num_validation(second_num):
    global num1
    global num2

    while True:
        try:
            if second_num == False:
                num1 = float(input("Please enter a number:").strip())
            else:
                num2 = float(input("Please enter a number:").strip())
            break
        except:
            print("Invalid input. Please enter a number.")

def symbol_validation():
    global symbol

    while True:
        print("""
        Enter one of the following:
        '+' to add.
        '-' to subtract.
        '*' to mulitply.
        '/' to divide.
        """)

        symbol = input("Enter symbol now:").strip()

        if symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/":
            break
        else:
            print("Invalid input.")

def math_function_call():
    global num1
    global num2
    global symbol

    if symbol == "+":
        add(num1, num2)
    elif symbol == "-":
        subtract(num1, num2)
    elif symbol == "*":
        multiply(num1, num2)
    else:
        divide(num1, num2)

def reset_calculator():
    global total
    total = 0.0

# Current while loop not needed but being set up to allow user to continue to build on total,
# reset total, etc. This will require refactoring in other places as well, but code still work
# as expected in the current form.
while True:

    num_validation(False)
    symbol_validation()
    num_validation(True)
    math_function_call()
    break
