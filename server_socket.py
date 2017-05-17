# Send and Receive Data using socket
# http://www.binarytides.com/python-socket-programming-tutorial/
#  A server is a system that uses sockets to receive incoming connections and provide them with data. 
import sys
import socket
from thread import *

HOST = ''
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind Failed. Error code: '+str(msg[0]) + ' Message ' +msg[1]
    sys.exit()
    
print 'Socket bind complete'

s.listen(10)
print 'Socket is listening'

# Fucntion for handling connections. Create threads

def clientthread(conn):
    #send message to client
    conn.send('Welcome to My server. Type something\n')
# wait to accept a connection
    while True:
        #conn, addr = s.accept()
        #print 'Connected with ' + addr[0] + ':' + str(addr[1])
    
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data:
            break
        conn.sendall(reply)
    conn.close()

while 1:
        conn, addr = s.accept()
        print 'Connected with ' +addr[0]+ ":"+ str(addr[1])
        start_new_thread(clientthread, (conn,))
s.close()