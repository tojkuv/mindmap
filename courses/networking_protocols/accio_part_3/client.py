#!/usr/bin/env python3

import sys, errno
import argparse
import socket

if __name__ == '__main__':

    # socket routine
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1)

        # socket connection
        try:
            client_socket.settimeout(10)
            client_socket.connect((sys.argv[1], int(sys.argv[2])))
            sys.stdout.write("socket connection established\n")
        except TimeoutError:
            sys.stderr.write("ERROR: timeout\n")
            sys.exit(1)
        except:
            sys.stderr.write(("ERROR: connection\n"))
            sys.exit(1)

        print(client_socket) # DEBUG

        input_buf = b''

        # waits for the first confirmation message
        while True:
            try:
                client_socket.settimeout(10)
                input_buf += client_socket.recv(1)

                if input_buf == b'accio\r\n':
                    input_buf = b''
                    break
            except TimeoutError:
                sys.stderr.write("ERROR: receive confirmation timeout\n")
                sys.exit(1)
            except:
                sys.stderr.write("ERROR: server disconnected\n")
                sys.exit(1)

        # sends the first confirmation message
        try:
            client_socket.settimeout(10)
            client_socket.send(b'confirm-accio\r\n')
        except TimeoutError:
            sys.stderr.write("ERROR: send confirmation timeout\n")
            sys.exit(1)
        except:
            sys.stderr.write("ERROR: server disconnected\n")
            sys.exit(1)

        # waits for the second confirmation message
        while True:
            try:
                client_socket.settimeout(10)
                input_buf += client_socket.recv(1)

                if input_buf == b'accio\r\n':
                    input_buf = b''
                    break
            except TimeoutError:
                sys.stderr.write("ERROR: receive confirmation timeout\n")
                sys.exit(1)
            except:
                sys.stderr.write("ERROR: server disconnected\n")
                sys.exit(1)

        # sends the second confirmation message
        try:
            client_socket.settimeout(10)
            client_socket.send(b'confirm-accio-again\r\n\r\n')
        except TimeoutError:
            sys.stderr.write("ERROR: send confirmation timeout\n")
            sys.exit(1)
        except:
            sys.stderr.write("ERROR: server disconnected\n")
            sys.exit(1)


        # attempts to send the file from CLI arguments
        with open(sys.argv[3], "rb") as fs:
            while True:
                client_socket.settimeout(10)
                out_buf = fs.read(10000)

                if out_buf == b'':
                    break

                while out_buf != b'':
                    sent_bytes = 0

                    try:
                        sent_bytes = client_socket.send(out_buf)
                        out_buf = out_buf[sent_bytes:]
                    except TimeoutError:
                        sys.stderr.write("ERROR: send data timeout\n")
                        sys.exit(1)
                    except:
                        sys.stderr.write("ERROR: server disconnected\n")
                        sys.exit(1)