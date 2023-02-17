import argparse
import socket
import selectors
import sys

sel = selectors.DefaultSelector()

counter = 0

class ClientData:
    def __init__(self, addr):
        self.addr = addr
        self.inb = b''
        self.outb = b''


def connect(sock, mask):
    # TODO: implement cli arguments
    sock.connect(("131.94.128.43", 54634))


def serviceConnection(key, mask):
    sock = key.fileobj
    data = key.data

    #TODO: wait for the client to receive 2 "accio\r\n" messages
    if mask & selectors.EVENT_READ:
        # TODO: implement 10 second timeout
        try:
            recv_data = sock.recv(1024)
            if recv_data:
                data.outb += recv_data
            else:
                print('closing connection to', data.addr)
                sel.unregister(sock)
                sock.close()
        except KeyError:
            sys.stderr.write('ERROR: ')
    
    # TODO: sent packages in 10_000 bytes
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing', repr(data.outb), 'to', data.addr)
            # TODO: implement 10 second timeout
            try:
                sent = sock.send(data.outb)
                data.outb = data.outb[sent:]
            except KeyError:
                sys.stderr.write('ERROR: ')



# TODO: implement commandline "<HOSTNAME-OR-IP> <PORT> <FILENAME>"
parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')


#TODO: exception handing for the hostname and port from the cli
# the file is always correct
# valid range for TCP port numbers (1-65535)
# ports are only 2 bytes 
try:
    pass
except KeyError:
    sys.stderr.write("ERROR: hostname or port is incorrect")



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print(clientSocket)

    # set socket to be non-blocking
    clientSocket.setblocking(False)

    # connect to the server
    sel.register(clientSocket, selectors.EVENT_READ, connect)
    events = sel.select(timeout = 10)


    # read the events from the read and write events from the connection
    while True:
        sel.register(clientSocket, selectors.EVENT_WRITE, serviceConnection)
        events = sel.select(timeout = 10)


#    sentLen = clientSocket.send(b"client message\r\n")
#    print("sent bytes", sentLen)


#    receivedLen = clientSocket.recv(1024)
#    print("bytes received", receivedLen)