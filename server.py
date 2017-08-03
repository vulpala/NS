__author__ = 'Harishiva'
# This is the Server program (Bob)
# importing packages
import socket
import sys
# importing Expo class from file expo
from expo import Expo

# creating a TCP/IP socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1200)

# binding the socket to the above port
sock.bind(server_address)

print >>sys.stderr, 'Starting up the socket connection on %s port %s' % server_address

# listen for incoming connections
sock.listen(1)

# These are the given values for g, sb, p
g = 1907
sb = 12067
p = 784313
print >> sys.stderr, 'Waiting for a client connection'
connection, client_address = sock.accept()
try:
    print >>sys.stderr, 'Connection from this client address', client_address

# receive the data and transmitting it
    data = connection.recv(1024)
    print >>sys.stderr, 'Received data"%s"' % data

# sending the data to the client
    message = Expo(g,sb,p)
    result = message.large_integer_exponent(g,sb,p)
    print ("Sending the result %s" % result)
    connection.sendall(str(result))

finally:
# closing the connection
    connection.close()