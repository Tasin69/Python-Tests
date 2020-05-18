import socket


#Making the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('data.pr4e.org', 80))
print('\nDialling pr4e..........................\n')

#Preparing and sending the data along with the protocol
#                               to establish connection
x = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
sock.send(x)


#Receiving and decoding data, each line containing upto 512 characters
while True:
    data = sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
sock.close