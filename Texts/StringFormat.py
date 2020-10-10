# Show a float number with different formats.

number = float(input('Introduce a number (float): '))

print(f'{number:.3f}')
print(f'{number:8.2f}')
print(f'{number:e}')
print(f'{number:010.4f}')
print(f'{number:20.5f}')