import cv2
import socket

import numpy

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("", 9901))

def reveice_save(s,sc):
	data,addr = s.recvfrom(64000)
	data = numpy.fromstring(data, dtype = 'uint8')
	image = cv2.imdecode(data, 1)
	print("haha")
	image = cv2.resize(image, (640,480))
	cv2.imshow(sc, image)
	cv2.imwrite('image_s.jpg', image)
	cv2.waitKey(10)

while True:
    reveice_save(s, "play")

    
