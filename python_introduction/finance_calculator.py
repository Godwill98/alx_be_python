
#PROMPT THE USER TO ENTER THEIR INCOME

monthly_income = float(input("Enter your monthly income: "))

##PROMPT THE USER TO ENTER THEIR EXPENSES

monthly_expenses = float(input("Enter your monthly expenses: "))


##CALCULATE THE MONTHLY SAVINGS

monthly_savings = monthly_income - monthly_expenses

Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your projected savings for the year is: {Projected_Savings}")