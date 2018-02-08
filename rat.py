#!/usr/bin/env python2.7

import socket
import os
import subprocess

host=''
port=1335

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "socket ok"
sock.bind((host,port))
sock.listen(5)
client,adresse=sock.accept()
print adresse

while 1:
  envs = raw_input('envoyer une commande, end pour arreter: \n')
  if envs=="end":
          break
  forw = client.send(envs)
  res = client.recv(4048)
  print 'resultat client' + res

sock.close()
client.close()

