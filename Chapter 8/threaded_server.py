import socket
import threading

class Client(threading.Thread):
    def __init__(self, client_sock, address):
        threading.Thread.__init__(self)
        self.client_sock = client_sock
        self.address = address

    def run(self):
        done = False
        while not done:
           data = self.client_sock.recv(size)
           data = data.decode('utf-8')
           if data == 'Exit':
               done = True
               done = True
           outstr = '*** ' + data
           self.client_sock.send(outstr.encode('utf-8'))
        self.client_sock.close()

host = 'localhost'
port = 2000
size = 512

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)

sock.bind(('',port))
sock.listen(5)
while True:
    client_sock, address = sock.accept()
    client_thread = Client(client_sock,address)
    client_thread.start()