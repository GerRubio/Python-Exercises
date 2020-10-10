# Calculate the total weight of the selected items.

CALCULATOR_WEIGHT = 112
CLOCK_WEIGHT = 75

calculator_quantity = int(input('Number of calculators: '))
clocks_quantity = int(input('Number of clocks: '))

total_calculators_weight = CALCULATOR_WEIGHT * calculator_quantity
total_clocks_weight = CLOCK_WEIGHT * clocks_quantity

total_weight = total_calculators_weight + total_clocks_weight

print(f'{total_weight} gr.')