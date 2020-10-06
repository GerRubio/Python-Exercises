VOWELS = 'aeiou'

word_phrase = input('Introduce something: ')
num_woels = 0

for i in word_phrase.lower():
    if i in VOWELS:
        num_woels += 1

print(num_woels)