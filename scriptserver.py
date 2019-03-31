import socket

class project_server(object):

    def __init__(self,host ="", port=8080):
        self._host, port =host, port
        self.address = (host, port)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(self.address)
        self.s.listen(5)

        print("server is connected")
        #self.gere_con()


    def handle_request(self):
        while True:
            clientsock, address = self.s.accept()
            print("Connect",address)
            clientsock.sendall(str(address + ">>>connected on server<<<"))

        while True:
            Message = clientsock.recv(500)

            if Message :
                print(">>>>  ")
            client.sendall(Message)
            clentsock.close()

            if __Bug__ == "__main__":
                try:
                    server = project_server()
                    server.start()
                except keyboardInterrupt:
                    exit()


something = project_server()
something.handle_request()
