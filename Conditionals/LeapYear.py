# Check if the entered year is a leap year.

year = int(input('Year: '))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('It is leap year.')
else:
    print('It is not a leap year.')