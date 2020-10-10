# Calculate the volume of a cylinder.

PI = 3.14

height = float(input('Height: '))
radius = float(input('Radius: '))

volume = PI * (radius ** 2) * height

print(f'Volume: {round(volume, 3)}')