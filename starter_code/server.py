# Server to implement a simple program that will carry out an exchange of
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

def PrimeCollect():
  """Accepts a prime number to send to the client"""
  primeNbr = input("Enter a prime number between 127 and 7919")
  return primeNbr

def GeneratorCollect():
  """Accepts a generator for the prime"""
  generator = input("Enter a generator for the prime number")
  return generator


def clientHello(g, p, x, r):
  """Generates an acknowledgement for the client heGeneratoressage"""
  msg = "105 Generator + Commitment "+ str(g) + ", " + str(p) + ", "+
          str(NumTheory.expMod(g,r,p)) + ", " + str(NumTheory.expMod(g,x,p))
  return msg

# r is the nonce chosen by the server
# x is the server's secret integer
# c is the client's challenge integer
def genChallengeResponse(r, x, c):
  """Generates the 107 LCM string"""
  z = r + c*x
  msg = "112 Response " + str(z)
  return msg

#s      = socket
#msg    = message being processed
#state  = dictionary containing state variables
def processMsgs(s, msg, state):
  """This function processes messages that are read through the socket. It returns
     a status, which is an integer indicating whether the operation was successful."""
  pass

def main():
  """Driver function for the server."""
  args = sys.argv
  if len(args) != 2:
    print ("Please supply a server port.")
    sys.exit()
  HOST = ''              #Symbolic name meaning all available interfaces
  PORT = int(args[1])    #The port on which the server is listening.
  if (PORT < 1023 or PORT > 65535):
    print("Invalid port specified.")
    sys.exit()

  print("Server of _____")
  with socket.socket('''specify socket parameters to use TCP''') as s:
    # Bind socket
    # listen
    conn, addr = # accept connections using socket
    with conn:
      print("Connected from: ", addr)
      #Process messages received from socket using 
      #  processMsgs(s, msg, state)
      
if __name__ == "__main__":
    main()