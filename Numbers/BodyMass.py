# Calculate body mass.

weight = float(input('Weight (kg): '))
height = float(input('Height (m): '))

body_mass = weight / (height * height)

print(f'Body Mass = {round(body_mass), 3}')