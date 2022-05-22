import socket

# Socket Setup
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 3000
hostname = '127.0.0.1' # Host IP
serverSocket.bind((hostname, port))
print('Listening at {}'.format(serverSocket.getsockname()))

def processInput():
    data, clientAddress = serverSocket.recvfrom(65535)
    print('> {}'.format(data.decode('ascii')))
    message = input(':')
    data = message.encode('ascii')
    serverSocket.sendto(data, clientAddress)

while True:
    processInput();
