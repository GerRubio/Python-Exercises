# Read a message by console and encrypt it with the Caesar method.

import string, sys 

ALPHABET = string.ascii_uppercase

# From line comand!
message = sys.argv[1].upper()
offset = int(sys.argv[2])

encoded_message = []

for letter in message:
    if letter.isalpha():
        letter_idx = ALPHABET.index(letter)
        encoded_letter_idx = (letter_idx + offset) % len(ALPHABET)
        encoded_letter = ALPHABET[encoded_letter_idx]
    else:
        # If contain spaces not codify.
        encoded_letter = letter
    
    encoded_message.append(encoded_letter)

# Convert to string.
encoded_message = ''.join(encoded_message)

print(f'Encoded message: {encoded_message}.')