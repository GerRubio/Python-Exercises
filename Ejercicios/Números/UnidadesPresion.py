kilopascals = float(input('Kilopascals: '))

kilopascals_to_pounds = round(kilopascals * 0.15, 3)
kilopascals_to_square_inches = round(kilopascals * 0.145, 3)
kilopascals_to_mercury_millimeters = round(kilopascals * 7501, 3)
kilopascals_to_atmosphere = round(kilopascals / 101, 3)

print(kilopascals, 'kilopascals =', kilopascals_to_pounds, 'pounds.')
print(kilopascals, 'kilopascals =', kilopascals_to_square_inches, 'square inches.')
print(kilopascals, 'kilopascals =', kilopascals_to_mercury_millimeters, 'mercury millimiters.')
print(kilopascals, 'kilopascals =', kilopascals_to_atmosphere, 'atmospheres.')