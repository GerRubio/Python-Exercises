# Calculate the volume of an area.

PI = 3.14

radius = float(input('Radius: '))

area = PI * radius ** 2
volume = 4 / 3 * (PI * radius ** 3)

print(f'Area is {round(area, 3)}')
print(f'Volume is {round(volume, 3)}')