# Calculate a factorial number with recursion.

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * (factorial(number - 1))

print(factorial(int(input('Number: '))))