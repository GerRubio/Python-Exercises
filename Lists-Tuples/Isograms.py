# Check if the sentence entered is a isogram.

sentence = input('Introduce a sentence: ')
letters = []

for iteration in sentence:
    if iteration in letters:
        print('It is not a isogram.')
        break
    
    letters.append(iteration)
else:
    print('It is a isogram.')