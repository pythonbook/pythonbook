import socket
import threading
import ssl

class Client(threading.Thread):
    def __init__(self, client_sock, address):
        threading.Thread.__init__(self)
        self.client_sock = client_sock
        self.address = address

    def run(self):
        done = False
        while done == False:
            data = self.client_sock.recv(size)
            data = data.decode('utf-8')
            if data == 'Exit':
                done = True
            outstr = '*** '+ data
            self.client_sock.send(outstr.encode('utf-8'))
        self.client_sock.close()

host = 'localhost'
port = 2000
size = 512

# create TLS context, load certificate
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.set_ciphers("DH:DSS:AES256:SHA")
context.load_cert_chain(certfile="certificate.pem",
                        keyfile="key.pem")


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',port))
sock.listen(5)
while True:
    client_sock, address = sock.accept()
    secure_sock = context.wrap_socket(client_sock,
                                      server_side=True)
    client_thread = Client(secure_sock,address)
    client_thread.start()