# Check if the word entered is a palindrome.

word = input('Introduce a word: ').lower()

if word == word[::-1]:
    print('It is palindrome.')
else:
    print('It is not a palindrome.')