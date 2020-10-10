# Read a dictionary that adds the total population of all cities and displays the contents of the dictionary.

cities_data = {
    'Tokyo': 38140000,
    'Delhi': 26454000,
    'Shanghai': 24484000,
    'Mumbai': 21357000,
    'São Paulo': 21297000
}

total_population = 0

# Total population.
for population in cities_data.values():
    total_population += population

# Relative population.
for city in cities_data:
    cities_data[city] = (cities_data[city] / total_population) * 100
    
print(f'Total population: {total_population}')
print(cities_data)