# Convert gallons to liters.

LITER = 3.785

gallons = float(input('Gallons to convert: '))

print(f'{gallons} gallons are {round(gallons * LITER, 3)}liters.')