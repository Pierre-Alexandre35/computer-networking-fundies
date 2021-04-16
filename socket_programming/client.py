import socket

# Initializations
TCP_IP = '192.168.1.99'
TCP_PORT = 8000
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
# Encode message string of Unicode format to UTF-8 format (Python uses this by default)
BYTE_MESSAGE = MESSAGE.encode()


SERVER_TCP_IP = '192.168.1.99'
SERVER_TCP_PORT = 8000


# 1. Create socket: Use IPv4 and Stream Socket (a TCP protocol for data transmission)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. Establish a connection with server
client_socket.connect((TCP_IP, TCP_PORT))

message = input("-> ")
while message !='q':
    # 3. Send data to socket
    encrypted_message = str.encode(message, 'utf-8')
    client_socket.sendto(encrypted_message, (SERVER_TCP_IP, SERVER_TCP_PORT))
    # 4. Recieve data from socket
    data = client_socket.recv(BUFFER_SIZE)
    # Decode message from UTF-8 to Unicode
    data = data.decode()
    # 5. Close the socket
    message = input("-> ")
client_socket.close()

print("Received data: {}".format(data))
print("Socket closed")