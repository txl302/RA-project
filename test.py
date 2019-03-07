import socket
from time import sleep

s_v = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

	s_v.sendto("haha", ("35.185.47.4", 9901))
	s_v.sendto("haha", ("192.168.1.124", 9901))
