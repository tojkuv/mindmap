#!/usr/bin/env python3

import sys
import socket
import signal
import threading
from selectors import DefaultSelector, EVENT_READ

def process_conn(conn_num, conn):
    while True:
        # sends the first confirmation message
        try:
            conn.send(b'accio\r\n')
        except TimeoutError:
            sys.stderr.write("ERROR: could not confirm the connection in time [send1]\n")
            conn.close()
            break

        # receives the first confirmation
        try:
            recv = b''
            while True:
                recv += conn.recv(1)

                if (recv == b'confirm-accio\r\n'):
                    recv = b''
                    break
        except TimeoutError:
            sys.stderr.write("ERROR: could not confirm the connection in time [recv1]\n")
            conn.close()
            break

        # sends the second confirmation message
        try:
            conn.send(b'accio\r\n')
        except TimeoutError:
            sys.stderr.write("ERROR: could not confirm the connection in time [send2]\n")
            conn.close()
            break

        # receives the second confirmation
        try:
            recv = b''
            while True:
                recv += conn.recv(1)

                if (recv == b'confirm-accio-again\r\n\r\n'):
                    recv = b''
                    break
        except TimeoutError:
            sys.stderr.write("ERROR: could not confirm the connection in time [recv2]\n")
            conn.close()
            break

        # receives and writes data to a file from the connection
        try:
            in_buff = b''

            while True:
                recv = conn.recv(10_000)
                if not recv:
                    break
                in_buff += recv

            conn.close()
            with open(sys.argv[2] + '/' + str(conn_num) + '.file', 'wb') as fs:
                fs.write(in_buff)
            break

        except TimeoutError:
            sys.stderr.write("ERROR: the server did not receive data in time after confirmation\n")
            conn.close()
            break
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


        # accepts up to 10 connections
        server_socket.listen(10)


        conn_counter = 0
        thread_list = list()

        while conn_counter <= 10:
            conn_counter +=1

            # accepts a connection
            try:
                conn, addr = server_socket.accept()
                conn.settimeout(10)
            except TimeoutError:
                sys.stderr.write("ERROR: accept client connection timeout [accept]\n")

            # creates a thread with the connection and add to a list of threads
            thread_list.append(threading.Thread(target=process_conn, args=(conn_counter, conn)))
            thread_list[len(thread_list) - 1].start()

        for thread in thread_list:
            thread.join()

        conn_counter = 0