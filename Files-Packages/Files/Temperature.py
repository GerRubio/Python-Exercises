# Calculate the average temps from a .txt file.

avg_temps = []

# Open the file.
with open('Temperatures.txt') as f:
    for line in f:
        monthly_temps = [int(data) for data in line.strip().split(',')]
        avg_temp = sum(monthly_temps) / len(monthly_temps)
        avg_temps.append(avg_temp)

# Create a new file with the result.
with open('AVGTemps.txt', 'w') as f:
    for avg_temp in avg_temps:
        f.write(f'AVG Temps: {avg_temp:.2f} \n')