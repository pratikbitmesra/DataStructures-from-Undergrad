# Send and Receive Data using socket
# http://www.binarytides.com/python-socket-programming-tutorial/
import sys
import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket with Error Code: ' + str(msg[0]) + ', Error message ' + msg[1]
    sys.exit()

print 'Socket Created'
host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    print 'HostName couldnt be rsolved.'
    sys.exit()

print 'IP address of ' + host + ' is ' + remote_ip
s.connect((remote_ip, port))
print 'Socket Connected to ' +host + ' on IP ' + remote_ip

# Send data to google
message = "GET /HTTP/1.1.\r\n\r\n"

try:
    s.sendall(message)
except socket.error:
    print 'Failed to Send data'
    sys.exit()

print 'Successfully sent'

reply = s.recv(4096)

print reply


