__author__ = 'Harishiva'
# This is the Client program (Alice)
# importing packages
import socket
import sys
# importing Expo class from file expo
from expo import Expo

# creating a TCP/IP socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1200)
print >> sys.stderr, 'Connecting to this server address %s port %s' % server_address

# connects the socket to the above port
sock.connect(server_address)
try:
    # sending data
    # these are the values given for g, sa, p
    g = 1907
    sa = 160011
    p = 784313
    message = Expo(g,sa,p)
    result = message.large_integer_exponent(g,sa,p)

    print ("Sending result %s" % result)
    # sends result to all the traffic
    sock.sendall(str(result))
    data = sock.recv(1024)

    print >> sys.stderr, 'Received data from server "%s"' % data

finally:
    print >> sys.stderr, 'closing the socket connection'
# closing the connection
    sock.close()