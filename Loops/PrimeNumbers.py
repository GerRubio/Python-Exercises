# Check if this number entered is prime and show every primer number since 1 till the number selected.

check_number = int(input('Number to check (int): '))
lower_number = int(input('Lower number (int): '))
upper_number = int(input('Upper number (int): '))

# Check if this number is prime.
for iteration in range(check_number // 2, 1, -1):    
    if check_number % iteration == 0:
        print(check_number, "It's not prime.")
        break
    else:
        print(check_number, "It's prime.")

# Show every primer number since 1 till the number selected.
for number in range(lower_number, upper_number + 1):
   if number > 1:
       for iteration in range(2, number):
           if (number % iteration) == 0:
               break
       else:
           print(f'Prime numbers are {number}')