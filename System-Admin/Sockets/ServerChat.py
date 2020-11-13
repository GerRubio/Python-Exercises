# Server.

import socket

ADDRESS = '127.0.0.1'
PORT = 8080

# Socket creation.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:

    socket_server.bind((ADDRESS, PORT))
    socket_server.listen()
    
    conn, addr = socket_server.accept()

    print(f'Conection from: {addr}')

    while True:
        data = conn.recv(1024)

        if data == b'':
            break

        print(f'Client sent: {data.decode("UTF-8")}')

        # Send information back to the client.
        message = str(input('New message: '))

        if message == 'S':
            break
        
        # String message to binary.
        message_bin = bytes(message, encoding = 'UTF-8')

        conn.send(message_bin)