# File name: WlanClient.py 
#
# This file provide client services as the interfaces between 
# the remote controller and the local controller for AR Drone. 
# The WiFi interface will exchange data messages with the peer 
# through the WiFi air link.
#
import socket
import time

# start the client socket service
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# the client socket at 192.168.1.110, port 8089
clientsocket.connect(('192.168.1.110', 8089))
# the client send a character 'r' to the socket
clientsocket.send('r')
# the client send a character '0' to the socket
clientsocket.send('0')

# end client service
print 'client service stops'
