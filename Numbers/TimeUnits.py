# Calculate the total seconds.

days = int(input('Days: '))
hours = int(input('Hours: '))
minutes = int(input('Minutes: '))
seconds = int(input('Seconds: '))

days_to_seconds = days * 86400
hours_to_seconds = hours * 3600
minutes_to_seconds = minutes * 60

total_time = days_to_seconds + hours_to_seconds + minutes_to_seconds

print(f'{days} D: {hours} HH: {minutes} MM: {seconds} SS = {total_time} {seconds}.')