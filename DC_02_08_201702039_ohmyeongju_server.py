import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('192.168.205.136', 9200))

name, addr = server_socket.recvfrom(2000)
print("File Name : ", name.decode())

data, addr = server_socket.recvfrom(2000)
size = int(data.decode())
print("File Size : ", size)

new_file = open(name, 'wb')

current_sum = 0
while True:
    try:
        file_save, addr = server_socket.recvfrom(2000)
        current_sum += len(file_save)
        success_rate = current_sum / size * 100
        if success_rate >= 100:
            print("current_size / total_size = ", current_sum, "/", size, ", ", "100.0%")
            break
        elif file_save == ' ':
            break
        new_file.write(file_save)
        print("current_size / total_size = ", current_sum, "/", size, ", ", success_rate, "%")
    except socket.timeout:
        break
new_file.close()
