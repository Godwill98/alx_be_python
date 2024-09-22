
#PROMPT THE USER TO ENTER THEIR INCOME

income = float(input("Please enter your monthly income: "))

##PROMPT THE USER TO ENTER THEIR EXPENSES

expenses = float(input("Please enter your monthly expenses: "))


##CALCULATE THE MONTHLY SAVINGS

monthly_savings = income - expenses

Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your projected savings for the year is: {Projected_Savings}")