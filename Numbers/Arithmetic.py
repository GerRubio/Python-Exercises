# Program that performs all mathematical operations.

from math import log10

a_number = float(input('A number: '))
b_number = float(input('B number: '))

print(f'Sum = {round(a_number + b_number, 3)}')
print(f'Subtraction = {round(b_number - a_number, 3)}')
print(f'Multiplication = {round(a_number * b_number, 3)}')
print(f'Division = {round(a_number / b_number, 3)}')
print(f'Rest = {round(a_number % b_number, 3)}')
print(f'Logarithm = {round(log10(a_number), 3)}')
print(f'Exponent = {round(a_number ** b_number), 3}')