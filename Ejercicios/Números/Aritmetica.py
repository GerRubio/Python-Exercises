from math import log10

a_number = float(input('A number: '))
b_number = float(input('B number: '))

print('Suma ', round(a_number + b_number, 3))
print('Resta' , round(b_number - a_number, 3))
print('Producto ', round(a_number * b_number, 3))
print('Cociente ', round(a_number / b_number, 3))
print('Resto ', round(a_number % b_number, 3))
print('Logaritmo ', round(log10(a_number), 3))
print('Exponente ', round(a_number ** b_number), 3)