from math import sqrt

side_1 = float(input('Side 1: '))
side_2 = float(input('Side 2: '))
side_3 = float(input('Side 3: '))

s = (side_1 + side_2 + side_3) / 2

area = s * (s - side_1) * (s - side_2) * (s - side_3)

final_area = sqrt(area)

print(round(final_area, 3))