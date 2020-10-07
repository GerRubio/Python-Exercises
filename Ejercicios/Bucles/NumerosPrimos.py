number = int(input('Number to check (int): '))
lower_number = int(input('Lower number (int): '))
upper_number = int(input('Upper number (int): '))

# Check if this number is prime.
for i in range(number // 2, 1, -1):    
    if number % i == 0:
        print(number, "It's not prime.")
        break
    else:
        print(number, "It's prime.")

# Show every primer number since 1 till the number selected.
for num in range(lower_number, upper_number + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)