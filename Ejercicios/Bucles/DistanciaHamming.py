# Check if the characters of two strings are equals and count how many differences between this two strings have.

first_text = "ABCD"
second_text = "DCBA"
counter = 0

for i in range(len(first_text)):
    if first_text[i] != second_text[i]:
        counter += 1

print(counter)