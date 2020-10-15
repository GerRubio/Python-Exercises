# Calculate the scale of a two integer lists.

v_1 = [4, 3, 8, 1]
v_2 = [9, 2, 7, 3]

result = 0

for zip_1, zip_2 in zip(v_1, v_2):
    result += zip_1 * zip_2

print(f'Result: {result}')