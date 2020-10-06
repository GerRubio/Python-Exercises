word = input('Word: ').lower()

if word == word[::-1]:
    print('It is palindrome.')
else:
    print('It is not.')
    