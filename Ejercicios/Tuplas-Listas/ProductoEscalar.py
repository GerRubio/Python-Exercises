v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]

result = 0

for i, j in zip(v1, v2):
    result += i * j

print(f'Result: {result}')