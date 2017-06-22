import socket
import time
from threading import Thread, Lock, active_count


# TODO neet to be implemented right
PRINT_LOCK = Lock()
SOCKET_LOCK = Lock()


def main():
    # define host and port to connect to.
    host = '127.0.0.1'
    port = 8888

    # create socket object
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server
    clientsocket.connect((host, port))
    st = Threads(clientsocket, 'send')
    rt = Threads(clientsocket, 'recv')
    print(active_count())

class Threads(Thread):
    def __init__(self, clientsocket, fn):
        Thread.__init__(self)
        self.clientsocket = clientsocket
        self.fn = fn
        self.start()

    def run(self):
        if self.fn == 'send':
            self.send()
        if self.fn == 'recv':
            self.recv()

    def recv(self):
        while True:
            # Receive 1024 bytes
            data = self.clientsocket.recv(1024).decode('UTF-8')
            if data:
                with PRINT_LOCK:
                    print('SERVER: {}'.format(data))
        self.clientsocket.close()
        exit(1)

    def send(self):
        # send data to socket
        while True:
            with PRINT_LOCK:
                msg = input('->')
            self.clientsocket.send(msg.encode('UTF-8'))
        self.clientsocket.close()
        exit(1)

if __name__ == '__main__':
    main()
