c_degrees = float(input('ºC degrees: '))

c_degrees_to_fahrenheit = round(c_degrees * (9 / 5) + 32, 3)
c_degrees_to_kelvin = round(c_degrees + 273.15, 3)

print(c_degrees, 'ºC degrees = ', c_degrees_to_fahrenheit, 'ºF degrees.')
print(c_degrees, 'ºC degrees = ', c_degrees_to_kelvin, 'ºK degrees.')