#!/bin/python3 

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("services.cyberprotection.agency", 9999))
data = s.recv(1024)
l = []
l.append(data.decode().strip())
nl = [i.encode('utf8') for i in l[0].split()]

v = int(nl[0].decode()) + int(nl[1].decode()) / int(nl[2].decode())
str(v)
#s.send(v.encode('utf-8'),("services.cyberprotection.agency", 9999))
#s.sendall(b'v',("services.cyberprotection.agency", 9999) )
s.sendall(b'v')
s.close()
