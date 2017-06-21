""" Server that handles the chat room"""
import socket
import time
from threading import Thread, Lock, current_thread ,active_count

#list of clients connected and socket Queue
CLIENTS = []
print_lock = Lock()

def main():
    '''
        Creates server socket and accepts connections
        as well as initializing Client_Handler(threads) each client socket
    '''
    # create  tcp socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # define host('' for all interfaces) and port
    host = ''
    port = 8888

    # bind socket to ip and port
    serversocket.bind((host, port))
    # allow socket to listen on connections
    # and set the limit for unaccepted connections before refusing connections
    serversocket.listen(5)

    # loop for accepting connections
    while True:
        # accepting and connection,
        # conn being a new socket and addr the bind address of it
        conn, addr = serversocket.accept()
        # add the new client socket to the clients list
        CLIENTS.append(conn)
        # create new Thread and start it as an daemon
        new_thread = Client_Handler(conn)
        with print_lock:
            print(active_count(), CLIENTS)

class Client_Handler(Thread):
    """ Handles the client sockets."""
    def __init__(self, socket):
        Thread.__init__(self)
        self._socket = socket
        self.daemon = True
        self.start()

    def run(self):
        self.loop()

    def auth_user(self):
        pass

    def loop(self):
        """
            Receive data and print it as well as reply a message
        """
        while True:
            # receive data from client and decode it
            try:
                data = self._socket.recv(1024).decode('UTF-8')
            except:
                break
            # print the received data
            with print_lock:
                print(data)
                print(active_count(), len(CLIENTS))
            # replay that data was recived
            self._socket.send('Message received'.encode('UTF-8'))

        # remove socket form CLient list
        CLIENTS.remove(self._socket)
        # close connection
        self._socket.close()
        return

if __name__ == '__main__':
    main()
