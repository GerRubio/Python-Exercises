# Calculate the distance between two points on Earth.

from math import sin, cos, sqrt, atan2, radians

# Radius of Earth in Km
R = 6373.0

lat_1 = float(input('Latitude 1: '))
lon_1 = float(input('Length 1: '))
lat_2 = float(input('Latitude 2: '))
lon_2 = float(input('Length 2: '))

radians(lat_1)
radians(lon_1)
radians(lat_2)
radians(lon_2)

dlon = lon_2 - lon_1
dlat = lat_2 - lat_1

a = sin(dlat / 2) ** 2 + cos(lat_1) * cos(lat_2) * sin(dlon / 2) ** 2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print(f'Distance: {round(distance, 3)} miles.')