from math import tan

PI = 3.14

s = float(input('S: '))
n = float(input('N: '))

dividen = n * s ** 2
divider = 4 * tan(PI / n)

result = round(dividen / divider, 3)

print(result)