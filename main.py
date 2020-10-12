import socket
from threading import *

# Se define un cliente genérico, que queda a la espera de saber si es el Arduino o un teléfono

class Cliente(Thread):
   def __init__(self, socket, direccion):
       Thread.__init__(self)

       self.socket = socket
       self.direccion = direccion
       self.start()

   def run(self):
       print("Nuevo Cliente")
       mensaje = self.socket.recv(10000).decode()

       # Cuando se establece la comunicación, el cliente primero debe enviar un mensaje informando su naturaleza: "Arduino" o "Móvil"
       if "Arduino" in mensaje:
           ClienteArduino(self.socket, self.direccion)
       elif "Movil" in mensaje:
           ClienteMovil(self.socket, self.direccion)
       elif mensaje != "":
           print("Sin cliente definido" + mensaje)

class ClienteMovil(Thread):
   def __init__(self, socket, direccion):
       Thread.__init__(self)

       self.socket = socket
       self.direccion = direccion
       self.start()

   def iniciar(self):
       print("El cliente se ha definido como teléfono")

       while True:
           # Se queda a la espera de recibir un mensaje
           mensaje = self.socket.recv(10000).decode()

           if mensaje != "":
               if mensaje == "acelerar":
                   # Próximamente incluir métodos de aceleración
                   pass

               if mensaje == "Cual es la temperatura actual" or mensaje == "cual es la temperatura " or mensaje == "Como esta el clima":
                   # Próximamente incluir métodos de aceleración
                   pass
                # Incluir las diversas funciones de la forma "if mensaje == "instruccion":
                # "instrucciones a ejecutar"

                
class ClienteArduino(Thread):
   def __init__(self, socket, direccion):
       Thread.__init__(self)

       self.socket = socket
       self.direccion = direccion
       self.start()


   def iniciar(self):
       print("El cliente se ha definido como arduino")
       while True:
           mensaje = self.socket.recv(10000).decode()
            
           # No se ha planteado que el arduino envie mensajes al servidor, pero esta instruccion se define para fines de depuracion y testeo
           if mensaje != "":
               print("Arduino:" + mensaje)

            
# Declaramos la direccion local (0.0.0.0) y el puerto que vamos a utilizar: Por defecto, en todo este trabajo, hemos definido el puerto 25000
direccionHost = "0.0.0.0"
puerto = 25000

# Iniciamos y dejamos el servidor a la escucha de nuevos clientes
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(direccionHost, puerto)
serversocket.listen(5)

# El servidor queda a la espera de nuevos clientes y los define de la clase "Cliente" (en otro Thread, para poder permitir concurrencia de clientes)
# Mas tarde, cuando el cliente envie sus datos ("Arduino" o "Movil"), este pasará a ser de la clase especifica que le corresponde
while True:
   cliente, direccionCliente = serversocket.accept()
   Cliente(cliente, direccionCliente)

