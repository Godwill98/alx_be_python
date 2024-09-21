# DRAWING PATTERNS WITH NESTED LOOPS

# GOAL: USE WHILE LOOPS AND NESTED FOR LOOPS TO CREATE A SIMPLE TEXT-BASED PATTERN.

# This Python script is named pattern_drawing.py. The script prompts the user for a positive integer
# and then uses nested loops to print a square pattern of that size using asterisks (*).

# INSTRUCTIONS:

# Prompt the user to input a positive integer that will determine the size of the pattern (i.e., the length of each side of the square).
size = int(input('ENTER THE SIZE OF THE PATTERN:'))

# Draw the pattern:
tracker = 0
# First, use a while loop to control the iteration through each row of the pattern.
while tracker < size:

    # Inside the while loop, use a for loop to print asterisks (*) next to each other without moving to a new line.
    for i in range(size):
        print('*', end='')
    
    # After printing each row, use print() to move to the next line.
    print()

    # Increment the tracker to move to the next row.
    tracker += 1
