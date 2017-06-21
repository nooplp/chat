import socket
import time


def main():
    # define host and port to connect to.
    host = '127.0.0.1'
    port = 8888

    # create socket object
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to server
    clientsocket.connect((host, port))

    # send data to socket
    while True:
        msg = input('->')
        clientsocket.send(msg.encode('UTF-8'))

        # Receive 1024 bytes
        print('SERVER: {}'.format(clientsocket.recv(1024).decode('UTF-8')))

    clientsocket.close()

if __name__ == '__main__':
    main()
