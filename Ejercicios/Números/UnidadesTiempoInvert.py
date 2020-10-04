seconds = int(input('Seconds: '))

seconds_to_minutes = round(seconds / 60)
seconds_to_hours = round(seconds / 3600)
seconds_to_days = round(seconds / 86400)

print(seconds, 'seconds =', seconds_to_days, 'D :', seconds_to_hours, 'HH :', seconds_to_minutes, 'MM')