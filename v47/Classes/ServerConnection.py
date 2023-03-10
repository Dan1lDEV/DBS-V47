import socket

import Configuration
from Classes.Connection import Connection


class ServerConnection:
    def __init__(self, address):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if Configuration.settings["DisableNagle"] == True:
            self.server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
        self.setupConnection(address)

    def setupConnection(self, address):
        self.server.bind(address)
        print("Сервер включён, ждём коннектов...")
        while True:
            self.server.listen()
            socket, address = self.server.accept()
            print("Новый коннект с адресом", address[0], "on port", address[1])
            Connection(socket, address).start()
