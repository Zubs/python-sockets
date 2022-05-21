import socket

# Socket Setup
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 3000
hostname = '127.0.0.1' # Host IP
serverSocket.bind((hostname, port))
print('Listening at {}'.format(serverSocket.getsockname()))

def processInput():
    data, clientAddress = serverSocket.recvfrom(65535)
    message = data.decode('ascii')
    uppercaseMessage = message.upper()
    data = uppercaseMessage.encode('ascii')
    print('The client at {} says {!r}'.format(clientAddress, message))
    serverSocket.sendto(data, clientAddress)

while True:
    processInput();
