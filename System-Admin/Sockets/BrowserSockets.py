# Web browser with sockets.

import socket, sys

PORT = 80

def get_web_site(web_site):
    
    # Socket creation.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client:     
        socket_client.connect((web_site, PORT))

        request = f'GET / HTTP/1.1 \r\n Host: {web_site} \r\n\r\n'

        socket_client.send(bytes(request, 'ASCII'))

        data = socket_client.recv(4096)

        return data.decode('ASCII').split('\r\n\r\n')[1]
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Use: {sys.argv[0]} example.com')
    else:
        print(get_web_site(sys.argv[1]))