# Removes the first items and the last two items from a list.

numbers_list = []

for _ in range(5):
    number = int(input('Introduce a number: '))
    numbers_list.append(float(number))

sorted_values = sorted(numbers_list)
print(f'List without outliers: {sorted_values}')

for _ in range(2):
    sorted_values.pop(-1)
    sorted_values.pop(0)

print(f'Result with outliers: {sorted_values}')