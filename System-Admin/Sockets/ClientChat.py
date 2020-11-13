# Client.

import socket

ADDRESS = '127.0.0.1'
PORT = 8080

# Socket creation.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client:

    socket_client.connect((ADDRESS, PORT))

    print('Write "S" to stop send information.')

    while True:
        message = str(input('New message: '))

        if message == 'S':
            break

        # String message to binary.
        message_bin = bytes(message, encoding = 'UTF-8') 
        
        socket_client.send(message_bin)

        # Information received from the server.
        data = socket_client.recv(4096)

        if data == b'':
            break

        print(f'Server send: {data}')