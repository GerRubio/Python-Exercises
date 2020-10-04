ELECTRICITY_COST = 8.9
J_KILOWATTS = 2778 * (10 ** -7)

energy = float(input('Energy (J): '))
mass = float(input('Mass (Kg): '))
temperature = float(input('Temperature (ºC): '))

c = -energy / (mass * -temperature)
j_result = c / (mass * temperature)
kw_result = j_result * J_KILOWATTS

print(round(j_result, 'J.'), 3)
print(round(kw_result, 'Kw.'), 3)
print(round(kw_result * ELECTRICITY_COST, 'cents.'), 3)