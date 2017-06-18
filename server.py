""" Server that handes the chat room"""
import socket
import time


#list of clients connected
CLIENTS = []

def main():
    ''' Creates server socket and accepts connections
        as well as initalizing threads each client socket
    '''
    # create  tcp socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # define host('' for all interfaces) and port
    host = ''
    port = 8888

    # define closing variabel
    closed = False

    # loop for accepting connections
    while not closed:
        # bind socket to ip and port
        serversocket.bind((host, port))
        # allow socket to listen on connections
        # and set the limit for unaccepted connectons before refusing connections
        serversocket.listen(5)
        # accepting and connection,
        # conn being a new socket and addr the bind address of it
        conn, addr = serversocket.accept()
        # add the new client socket to the clients list
        CLIENTS.append((conn, addr))
        closed = True

def recv_redirect(socket):
    """ Target function of client socket threads.
        Relays the recived message to the wanted partner.
        If thats not possible inform sender.

        socket -- client socket of the thread
    """
    # recive data from client and decode it
    data = socket.recv(1024).decode('UTF-8')
    # print the recived data
    print(data)
    # replay that data was recived
    socket.send('Message receved, closing connection'.encode('UTF-8'))
    #close connection
    socket.close()


if __name__ == '__main__':
    main()
    recv_redirect(CLIENTS[0][0])
