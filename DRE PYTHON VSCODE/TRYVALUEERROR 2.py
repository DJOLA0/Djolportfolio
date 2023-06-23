# # A code for users to pick two numbers and an operator 
# AND record them to one file with the format 10 * 5 = 50

def validate_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("oops! That was not a valid number. Try again...")


import math

while True:
    print("Welcome, press 1 to run calculation or 2 to read from file, or 3 to exit.")
    choice = input(">___")
    # ask them for a file name that they want to use to store the equations.
    if choice == "2":
        while True:
            filename = input("provide a filename you want to put the equation in: ")

            try:
                with open(filename, 'r') as file:
                    contents = file.read()
                    print(contents)
                    break
            except FileNotFoundError:
                print("File does not exist. Please enter the correct file name")

    elif choice == "1":
        valid_number = False
        # Get the user's first number
        # operator conditions for while loop.
        first_number = validate_int("Please enter number 1: ")
        second_number = validate_int("Please enter number 2: ")

        operator_list = ["+", "-", "*", "/"]
        valid_operator = False
        # Ask the user which operation they want to use
        while not valid_operator:
            operator = input("Enter an operator for your equation: ")
            if operator in operator_list:
                valid_operator = True
            else:
                print("Pick a valid operator.")

            if operator == '+':
                result = first_number + second_number
                print(first_number, operator, second_number, "=", result)
            elif operator == '-':
                result = first_number - second_number
                print(first_number, operator, second_number, "=", result)
            elif operator == '*':
                result = first_number * second_number
                print(first_number, operator, second_number, "=", result)
            elif operator == '/':
                if second_number == 0:
                    print("Division by 0 error")
                    result = first_number / second_number
                    print(first_number, operator, second_number, "=", result)
            else:
                print("Please enter a valid operator")

            with open("test.txt", "w") as file:
                file.write(first_number, operator, second_number, "=", result)

    elif choice == "3":
        break