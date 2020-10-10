# Convert from feet to cm and convert from inches to cm.

FEET_CENTIMETER = 30.48
INCHES_CENTIMETER = 2.54

feet_quantity = float(input('Feet: '))
inches_quantity = float(input('Inches: '))

feet_to_cm = round(feet_quantity * FEET_CENTIMETER, 3)
inches_to_cm = round(inches_quantity * INCHES_CENTIMETER, 3)

print(f'{feet_quantity} feet are {feet_to_cm} "cm".')
print(f'{inches_quantity} inches are {inches_to_cm} "cm".')