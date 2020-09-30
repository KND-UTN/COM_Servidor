import socket
from threading import *


class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        msg = self.sock.recv(10000).decode()
        if msg == '':
            print('Cliente cerrado')
        else:
            print('Mensaje recibido:', msg)
            dividido = msg.split(",")
            if len(dividido) == 2:
                # Las peticiones se van a basar en mensajes de dos partes, separados por comas
                # La primera parte es el numero de instruccion, la segunda parte son parametros (Si son necesarios)

                # Instruccion 0
                if dividido[0] == '0':
                    mensaje = str.encode("Esto es lo que se va a dar como respuesta")
                    self.sock.send(mensaje)
                    self.sock.close()

                # Instruccion 1
                if dividido[0] == '1':
                    mensaje = str.encode("Esto es lo que se va a dar como respuesta")
                    self.sock.send(mensaje)
                    self.sock.close()

                # Instruccion 2
                if dividido[0] == '2':
                    mensaje = str.encode("Esto es lo que se va a dar como respuesta")
                    self.sock.send(mensaje)
                    self.sock.close()

                # Instruccion 3
                if dividido[0] == '3':
                    mensaje = str.encode("Esto es lo que se va a dar como respuesta")
                    self.sock.send(mensaje)
                    self.sock.close()


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "0.0.0.0"
port = 23000
serversocket.bind((host, port))

serversocket.listen(5)
print('Servidor iniciado, esperando...')
while 1:
    clientsocket, address = serversocket.accept()
    print('Anadido')
    client(clientsocket, address)
