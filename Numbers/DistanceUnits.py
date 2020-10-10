# Transform feet into yards and miles.

FEET_INCHES = 12
YARDS_INCHES = 3
MILES_INCHES = 5280

feet_quantity = float(input('Feet: '))

feet_to_inches = round(feet_quantity * FEET_INCHES, 3)
feet_to_yards = round(feet_quantity / YARDS_INCHES, 3)
feet_to_miles = round(feet_quantity / MILES_INCHES, 3)

print(f'{feet_quantity} feet are {feet_to_inches} inches.')
print(f'{feet_quantity} feet are {feet_to_yards} yards.')
print(f'{feet_quantity} feet are {feet_to_miles} miles.')