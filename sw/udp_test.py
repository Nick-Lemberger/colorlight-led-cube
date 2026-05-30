#!/bin/python3.7
import socket
import numpy as np

UDP_IP = '192.168.178.50'
UDP_PORT = 2000


num_rows = 64
num_cols = num_rows
output_size = num_rows

header_size = 2
data_size = 3
hbuf = np.zeros((1, header_size), dtype=np.uint8)
dbuf = np.zeros((num_rows, data_size), dtype=np.uint8)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

r = np.uint8(30)
g = np.uint8(30)
b = np.uint8(30)
panel = np.uint8(0)
addr = np.uint8(0)

#while(1):
for y in range(int(num_rows)):
    for x in range(num_cols):
        panel = 1
        r = x*4*0
        g = x*4*0
        b = x*4
        dbuf[x] = [b,g,r]
    packet = bytes([panel, y]) + dbuf.tobytes() # Header + data payload
    #print(packet)
    s.sendto(packet, (UDP_IP, UDP_PORT))
exit()





