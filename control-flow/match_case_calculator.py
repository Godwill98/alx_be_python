# OBJECTIVE: LEARN TO USE MATCH CASE STATEMENTS TO HANDLE MULTIPLE OPERATIONS IN A SIMPLE CALCULATOR PROGRAM.

# This Python script is named match_case_calculator.py.
# The calculator will prompt the user to enter two numbers and choose an operation (addition, subtraction, multiplication, or division).
# Using a match-case statement, the script will perform the selected operation and display the result.

# TASK DESCRIPTION:

# Prompt the user to input two numbers (one at a time) with the following prompts: "Enter the first number:" and "Enter the second number:".

num1 = int(input('Enter the first number:'))  
num2 = int(input('Enter the second number:'))

# Ask the user to choose the operation they'd like to perform by entering one of these symbols: +, -, *, /.

operation = input('Choose the operation (+, -, *, /):')

# Use a match-case statement to perform the corresponding operation based on the user’s input.

match operation: 
    case '+':
        result = num1 + num2
        print(f'The result is {result}.')
    case '-':
        result = num1 - num2
        print(f'The result is {result}.')
    case '*':
        result = num1 * num2
        print(f'The result is {result}.')
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f'The result is {result}.')
        else:
            print('Cannot divide by zero.')
