import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("", 9901))

while True:
    data,addr = s.recvfrom(64000)
    print(data)

    
