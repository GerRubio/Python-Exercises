# Calculate the area of a room.

room_length = float(input('Length of the room: '))
room_width = float(input('Width of the room: '))

room_area = round(room_length * room_width, 3)

print(f'Area: {room_area}')