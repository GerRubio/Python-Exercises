# Return the first 100 even numbers with a generator. 

def even_numbers():
    iterator = 0
    
    for _ in range(0, 100, 2):
        iterator += 2
        yield iterator

# Function saved into a variable
generator = even_numbers()

for number in generator:
    print(number)