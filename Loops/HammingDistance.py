# Check if the characters of two strings are equals and count how many differences between this two strings have.

first_text = 'ABCD'
second_text = 'DCBA'
counter = 0

for iteration in range(len(first_text)):
    if first_text[iteration] != second_text[iteration]:
        counter += 1

print(f'{counter} differencies.')