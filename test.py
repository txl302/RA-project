import socket

s_v = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    s_v.sendto("haha", ("192.168.1.124", 9901))

    sleep(1)