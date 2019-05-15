import socket
import os

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = '192.168.205.136'
port = 9200

name = input("Input your file name : ")
size = os.path.getsize(name)

print("File Transmit Start....")
client_socket.sendto(name.encode(), (ip, port))
client_socket.sendto(str(size).encode(), (ip, port))

file_open = open(name, 'rb')
#file_restore = file_open.read(1024)

current_sum = 0
while True:
    file_save = file_open.read(1024)
    current_sum += client_socket.sendto(file_save, (ip, port))
    success_rate = current_sum / size * 100
    if success_rate >= 100:
        print("current_size / total_size = ", current_sum, "/", size, ", ", "100.0%")
        break
    print("current_size / total_size = ", current_sum, "/", size, ", ", success_rate, "%")
    #current_sum += current_socket.sendto(file_restore, (ip, port))

    
print("ok")
print("file_send_end")
file_open.close()
