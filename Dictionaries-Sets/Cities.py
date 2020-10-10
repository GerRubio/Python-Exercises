# Create a dictionary wiht cities and their population.

cities_list = {}

for _ in range(3):
    city_name = (input('Introduce a city name: '))
    city_population = int(input('Introduce a citiy population: '))

    cities_list[city_name] = city_population

print(cities_list)