import socket
import time


def main():
    # define host and port to connect to.
    host = '127.0.0.1'
    port = 8888

    # create socket object
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connct to server
    clientsocket.connect((host, port))

    # send data to socket
    clientsocket.send('Hello I sent this.'.encode('UTF-8'))

    # Receive 1024 bytes
    print('SERVER: {}'.format(clientsocket.recv(1024).decode('UTF-8')))

    clientsocket.close()

if __name__ == '__main__':
    main()
