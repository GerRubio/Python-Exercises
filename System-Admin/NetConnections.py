# Get a NET Stat.

import psutil, socket

print('PROTOCOLO \t LOCAL ADDRESS \t FOREIGN ADDRES \t STATUS')

for info in psutil.net_connections():
    if info.type == socket.SOCK_STREAM:
        proto = 'TCP'
    elif info.type == socket.SOCK_DGRAM:
        proto = 'UDP'
    try:
        print(f'{proto} \t {info.laddr.ip}:{info.laddr.port} \t {info.raddr.ip}:{info.raddr.port} \t {info.status}')
    except AttributeError:
        print(f'{proto} \t {info.laddr.ip}:{info.laddr.port} \t 0.0.0.0:- \t {info.status}')