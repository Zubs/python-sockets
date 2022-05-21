import socket

# Socket setup
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter a sentence: ")
data = message.encode('ascii')
clientSocket.sendto(data, ('127.0.0.1', 3000))
data, address = clientSocket.recvfrom(65535)
text = data.decode('ascii')
print('The server, {}, responded with {!r}'.format(address, text))
