import socket

host = 'localhost'
port = 2000
size = 512

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)

sock.connect((host,port))

done = False
while not done:
    data = input('Enter string: ')
    if data == 'Exit':
        done = True
    sock.send(data.encode('utf-8'))
    data = sock.recv(size)
    print('Received: ' + data.decode('utf-8'))
        
sock.close()