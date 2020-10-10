# Calculate the taxes of a meal.

TAX_RATE = 0.07
TIP_RATE = 0.05

meal_cost = float(input('Please input the cost of the meal: '))

tip = meal_cost * TIP_RATE
tax = meal_cost * TAX_RATE
total_cost = meal_cost + tip + tax

print(f'Raw meal cost: {round(meal_cost), 3}')
print(f'Tip: {round(tip, 3),} €.')
print(f'Tax: {round(tax, 3)} €.')
print(f'Total cost: {round(total_cost, 3)} €.')