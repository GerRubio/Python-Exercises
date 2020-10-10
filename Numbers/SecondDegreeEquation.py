# Second degree equation program.

from math import sqrt

a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

dividend_positive = -b + sqrt((b ** 2) - (4 * a * c))
dividend_negative = -b - sqrt((b ** 2) - (4 * a * c))
divider = 2 * a

result_positive = dividend_positive / divider
result_negative = dividend_negative / divider

print(f'Positive: {result_positive}')
print(f'Negative: {result_negative}')