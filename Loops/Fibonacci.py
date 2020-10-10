# Show Fibonacci sequence.

first_number = 0
print(first_number)

second_number = 1
print(second_number)

for _ in range(98):
    result = first_number + second_number
    first_number = second_number
    second_number = result

    print(result)