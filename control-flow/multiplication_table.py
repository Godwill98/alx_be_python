number = int(input('enter a number to see its multiplication table:')) 

#! USE A FOR LOOP TO ITERATE THROUGH THE NUMBERS 1 TO 10.
for i in range(1, 11):

    #! Print each line of the multiplication table in the format: “X * Y = Z”
    print(f"{number} * {i} = {number * i}")   