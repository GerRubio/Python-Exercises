# Count how many vowels there are in the entered sentence.

VOWELS = 'aeiou'

sentence = input('Introduce something: ')
num_vowels = 0

for iteration in sentence.lower():
    if iteration in VOWELS:
        num_vowels += 1

print(f'Number of vowles: {num_vowels}')