import socket

host = 'localhost'
port = 2000
size = 512

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)

sock.bind(('',port))
sock.listen(5)
while True:
    client_sock, address = sock.accept()
    done = False
    while not done:
        data = client_sock.recv(size)
        data = data.decode('utf-8')
        if data == 'Exit':
            done = True
        outstr = '*** ' + data
        client_sock.send(outstr.encode('utf-8'))