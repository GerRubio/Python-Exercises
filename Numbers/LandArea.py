# Calculate the area of a land.

SQFEET_TO_ACRES = 2.29568e-05

field_length = float(input('Length of the field (square feet): '))
field_width = float(input('Width of the field (square feet): '))

field_area_in_feet = field_length * field_width
field_area_in_acres = field_area_in_feet * SQFEET_TO_ACRES

print(f'{round(field_area_in_acres, 3)} acres.')