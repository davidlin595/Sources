# File name: WlanServer.py 
#
# This file provide server services as the interfaces between 
# the remote controller and the local controller for AR Drone. 
# The WiFi interface will exchange data messages with the peer 
# through the WiFi air link.
#
import socket
import time

# start the server socket service
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# the server socket at 192.168.1.110, port 8089
serversocket.bind(('192.168.1.110', 8089))
# become a server socket, maximum 5 connectio
serversocket.listen(5) 

# start server loop
while True:
    # waiting for the link establishment with client
    connection, address = serversocket.accept()
    # waiting for receiving data from the client
    buf = connection.recv(64)
    # print message 'move right' if receiving a character 'r'
    if buf == 'r':
        print 'move right'
    # break the loop if receiving a character '0'
    if len(buf) == '0':
        print 'invalid command'
        break

# end server service
print 'server service stops'
