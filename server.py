import socket
import math
import os

server_adddress = ('127.0.0.1', 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_adddress)

filename, client_address = server_socket.recvfrom(1024)
filename = filename.decode()

size, client_address = server_socket.recvfrom(1024)
size = int(size.decode())

loop = math.ceil(float(size) / 1024)

text = ""

for i in range(loop):
    data_message, client_address = server_socket.recvfrom(1024)
    text = text + str(data_message, 'utf-8')

cwd = os.getcwd()
f = open(cwd + "\\output\\" + filename, "w")
f.write(text)
f.close()

size_received = os.path.getsize(cwd + "\\output\\" + filename)

print("Percentage of data received: " + str((size_received/size) * 100) + "%")