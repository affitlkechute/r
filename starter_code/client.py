# Client to implement a simple program that will carry out an exchange of
# messages that contains elements of a zero knowledge
# proof. The client sends a hello message to the server. The server responds
# with a message containing a generator, a prime, some public information, and
# a "commitment" message. The client will respond with a challenge message that
# contains an integer. The server transforms that received integer and then
# sends a response message to the client. The client checks that this
# transformed integer shows that the server knows the secret (without the
# secret being revealed).

# Author: fokumdt
# Last modified: 2024-10-14
#!/usr/bin/python3

import socket
import sys
from random import SystemRandom
from NumTheory import NumTheory

def serverHello():
  """Generates server hello message"""
  status = "100 Hello"
  return status

def AllGood():
  """Generates 220 Verified"""
  status = "220 OK"
  return status

def ErrorCondition():
  """Generates 400 Error"""
  status = "400 Error"
  return status

def ChallengeMsg(c):
  """Generates 111 Challenge """
  status = "111 Challenge " + str(c)
  return status
 
# s     = socket
# msg   = message being processed
# state = dictionary containing state variables
def processMsgs(s, msg, state):
  """This function processes messages that are read through the socket. It
     returns a status, which is an integer indicating whether the operation
     was successful."""
  pass

def main():
  """Driver function for the project"""
  args = sys.argv
  if len(args) != 3:
    print("Please supply a server address and port.")
    sys.exit()
  serverHost = str(args[1])  #The remote host
  serverPort = int(args[2])  #The port used by the server
  print("Client of _____")
  print("""
  The purpose of this program is to collect two prime numbers from the client, and then
  send them to the server. The server will compute their LCM and send it back to the
  client. If the server-computed LCM matches the locally computed LCM, the
  clientsends the server a 200 OK status code. Otherwise it sends a 400 error status code,
  and then closes the socket to the server.
  """)
  #Add code to initialize the socket
  msg = serverHello()
  #Add code to send data into the socket

  #Handle the data that is read through the socket by using processMsgs(s, msg, state)

  #Close the socket
if __name__ == "__main__":
    main()
  