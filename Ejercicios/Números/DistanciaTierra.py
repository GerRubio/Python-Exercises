from math import sin, cos, sqrt, atan2, radians

# Radius of Earth in Km
R = 6373.0

lat1 = float(input('Latitude 1: '))
lon1 = float(input('Length 1: '))
lat2 = float(input('Latitude 2: '))
lon2 = float(input('Length 2: '))

radians(lat1)
radians(lon1)
radians(lat2)
radians(lon2)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print('Distance: ', round(distance, 3), 'miles')