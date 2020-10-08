A = [[6, 4], [8, 9]]
B = [[3, 2], [1, 7]]

element_00 = A[0][0] * B[0][0] + A[0][1] * B[1][0]
element_01 = A[0][0] * B[0][1] + A[0][1] * B[1][1]
element_10 = A[1][0] * B[0][0] + A[1][1] * B[1][0]
element_11 = A[1][0] * B[0][1] + A[1][1] * B[1][1]

result = [[element_00, element_01], [element_10, element_11]]

print(f'Result: {result}')