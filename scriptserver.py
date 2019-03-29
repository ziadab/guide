import socket

class project_server(object):

    def __init__(self,host ="", port=8080):
        self._host, port=host, port
        self.address = (host, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsckopt(sockt.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def ___INIT___(self):
        self.sock.bind(self.address)
        self.sock.listen(5)

        print "server is connected"
        self.gere_con()

    def handle_request(self):
        while True:
            clientsock, address = self.sock.accept()
            print("Connect",address)
            clientsock.sendall(str(address + ">>>connected on server<<<"))

        while True:
            Message = clientsock.recv(500)

            if Message :
                print ">>>>  "
            client.sendall(Message)
            clentsock.close()

            if __Bug__ == "__main__":
                try:
                    server = project_server()
                    server.start()
                except keyboardInterrupt:
                    exit()
