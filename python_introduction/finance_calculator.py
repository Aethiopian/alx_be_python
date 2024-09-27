# Prompt the user for their financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% interest
annual_savings = monthly_savings * 12  # Total savings in a year
projected_savings = annual_savings + (annual_savings * 0.05)  # Adding 5% interest

# Output results
print(f"Your monthly savings: {monthly_savings:.2f}")
print(f"Projected annual savings after including interest: {projected_savings:.2f}")
