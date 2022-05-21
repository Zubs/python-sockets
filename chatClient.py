import socket

# Socket setup
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.connect(('127.0.0.1', 3000))

def chat():
    message = input(':')
    data = message.encode('ascii')
    clientSocket.send(data)
    data, serverAddress = clientSocket.recvfrom(65535)
    text = data.decode('ascii')
    print('> {}'.format(text))
    

while True:
    chat()
