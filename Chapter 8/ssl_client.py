import socket
import ssl
import pprint

host = 'localhost'
port = 2000
size = 512

#grab and return certificate if user asks
data = input("Show server certificate? (Y/N)")
if (data == 'Y' or data == 'y'):
    print(ssl.get_server_certificate((host,port)))

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)

# create TLS context, wrap around socket
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.set_ciphers("DH:DSS:AES256:SHA")
secure_sock = context.wrap_socket(sock)

secure_sock.connect((host,port))

done = False
while not done:
    data = input('Enter string: ')
    if data == 'Exit':
        done = True
    secure_sock.send(data.encode('utf-8'))
    data = secure_sock.recv(size)
    print('Received: ' + data.decode('utf-8'))
    
secure_sock.close()