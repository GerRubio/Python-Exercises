word = 'lumberjacks'
letters = []

for i in word:
    if i in letters:
        print("It is not a isogram")
        break
    
    letters.append(i)
else:
    print("It is a isogram.")
