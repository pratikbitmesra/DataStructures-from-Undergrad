# http://www.binarytides.com/python-socket-server-code-example/
# Handle multiple socket clients with select function using polling
import socket, select

if __name__ == "__main__":
    
    CLIENTS = []
    RECV_BUFFER = 4096
    PORT = 15000
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)
    
    CLIENTS.append(server_socket)
    
    print "Chat Server Started on Port " + str(PORT)
    
    while 1:
        read_sockets,write_sockets,error_sockets = select.select(CLIENTS,[],[])
        
        for sock in read_sockets:
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                CLIENTS.append(sockfd)
                print "Client (%s, %s) connected"%addr
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        sock.send('OK... '+data)
                except:
                    broadcast_data(sock, "Client (%s, %s) is offline" %addr)
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CLIENTS.remove(sock)
                    continue
    server_socket.close()