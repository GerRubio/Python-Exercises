# Add the prime positive numbers of another number.

number = int(input('Enter a positive integer: '))

sum = (number * (number + 1)) // 2

print(f'Sum of first {number} positive integers: {sum}')