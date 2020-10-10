# Show all multiplication tables.

for number in range(11):
    for multiplication in range(11):
        result = number * multiplication       
        print(number, 'X', multiplication, '=', result)
    
    print('----------')