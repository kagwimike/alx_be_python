# finance_calculator.py
# This script calculates monthly and projected annual savings based on user input.
# Author: [Your Name]
# Repository: alx_be_python
# Directory: python_introduction

# Prompt user for input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Annual projection with 5% interest
annual_interest_rate = 0.05
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Display results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")
