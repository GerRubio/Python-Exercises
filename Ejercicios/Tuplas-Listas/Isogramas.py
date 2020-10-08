sentence = input('Insert a sentence: ')
letters = []

for i in sentence:
    if i in letters:
        print('It is not a isogram.')
        break
    
    letters.append(i)
else:
    print('It is a isogram.')
