#!/usr/bin/env python3

import sys
import socket
import signal
import threading
from selectors import DefaultSelector, EVENT_READ

def process_conn(conn_num, server_socket):
    while True:
        # accept a connection
        try:
            conn, addr = server_socket.accept()
            conn.settimeout(10)
        except TimeoutError:
            sys.stderr.write("ERROR: accept client connection timeout\n")


        # sends the first confirmation message
        try:
            conn.send(b'accio\r\n')
        except TimeoutError:
            sys.stderr.write("ERROR: could not confirm the connection in time\n")
            conn.close()

        # receives the first confirmation
        try:
            recv = b''
            while True:
                recv += conn.recv(1)

                if (recv == b'confirm-accio\r\n'):
                    recv = b''
                    break
        except TimeoutError:
            sys.stderr.write("ERROR: could not confirm the connection in time\n")

        # sends the second confirmation message
        try:
            conn.send(b'accio\r\n')
        except TimeoutError:
            sys.stderr.write("ERROR: could not confirm the connection in time\n")
            conn.close()

        # receives the second confirmation
        try:
            recv = b''
            while True:
                recv += conn.recv(1)

                if (recv == b'confirm-accio-again\r\n\r\n'):
                    recv = b''
                    break
        except TimeoutError:
            sys.stderr.write("ERROR: could not confirm the connection in time\n")

        # receives and prints data from the connection
        try:
            in_buff = 0

            while True:
                recv = conn.recv(10_000)
                if not recv:
                    break
                in_buff += len(recv)

            conn.close()
            # TODO: user the handle argument from the cli to save save the data to a file in that directory
            #  (named based on the connection number)
            print(in_buff)
        except TimeoutError:
            sys.stderr.write("ERROR: the server did not receive data in time after confirmation\n")
            conn.close()
            # TODO: create an empty file (named based on the connection number)


if __name__ == '__main__':
    # event handlers
    def sigquit_handler(signum, frame):
        sys.stderr.write("ERROR: main thread terminated\n")
        raise SystemExit
    signal.signal(signal.SIGQUIT, sigquit_handler)

    def sigtrem_handler(signum, frame):
            sys.stderr.write("ERROR: main thread terminated\n")
            raise SystemExit
    signal.signal(signal.SIGTERM, sigtrem_handler)

    def sigint_handler(signum, frame):
        sys.stderr.write("ERROR: Exited with keyboard interrupt\n")
        raise KeyboardInterrupt
    signal.signal(signal.SIGINT, sigint_handler)


    # creates a socket routine
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            server_socket.bind(("0.0.0.0", int(sys.argv[1])))
        except:
            sys.stderr.write("ERROR: incorrect port: %s" % sys.argv[1])
            sys.exit(1)


        # accept up to 10 connections
        server_socket.listen(10)


        # socket connections processing threads
        conn_counter = 0
        thread_list = list()

        while conn_counter <= 10:
            conn_counter +=1

            thread_list.append(threading.Thread(target=process_conn, args=(conn_counter, server_socket)))
            thread_list[len(thread_list) - 1].start()

        for thread in thread_list:
            thread.join()

        conn_counter = 0