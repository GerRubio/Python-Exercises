TAX_RATE = 0.07
TIP_RATE = 0.05

meal_cost = float(input('Please input the cost of the meal: '))
tip = meal_cost * TIP_RATE
tax = meal_cost * TAX_RATE
total_cost = meal_cost + tip + tax

print('Raw meal cost: ', round(meal_cost), 3)
print('Tip:', round(tip, 3), '€')
print('Tax:', round(tax, 3), '€')
print('Total cost:', round(total_cost, 3), '€')