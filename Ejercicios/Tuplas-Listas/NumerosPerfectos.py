import sys

number = int(sys.argv[1])
perfect_numbers = []

for number in range(1, number +1):
    dividers = [divider for divider in range(1, number // 2, 1) if number % 1 == 0]   

    # TODO: Result

# print(f'Perfect numbers of {number} are {dividers}')            