import json
import socket
import time
from threading import *
import Dolar
import Clima
import ManejoWEB


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

        # Cuando se establece la comunicación, el cliente
        # primero debe enviar un mensaje informando su naturaleza:
        # "Arduino" o "Móvil"

        if "Arduino" in mensaje:
            AdministradorArduino.asignarArduino(ClienteArduino(self.socket, self.direccion))
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

    def run(self):
        print("El cliente se ha definido como telefono")

        while True:

            # el mensaje que nos manda es en binario y lo queremos en texto, por eso usamos el decode
            # Se queda a la espera de recibir un mensaje
            mensaje: str = self.socket.recv(10000).decode()
            # mensaje es lo que le mandamos al servidor

            if mensaje != "":
                if mensaje == "acelerar":
                    mensajeEnviar = {'instruccion': 'acelerar'}

                elif mensaje == "frenar":
                    mensajeEnviar = {'instruccion': 'frenar'}

                elif "temperatura" in mensaje.lower() or "clima" in mensaje:
                    # aca el arduino muestra el clima
                    vectorcito = Clima.obtener_clima('Córdoba, arg')
                    mensajeEnviar = {'instruccion': 'clima', 'temperatura': vectorcito[0], 'humedad': vectorcito[1]}

                elif "dólar" in mensaje.lower():
                    precio = Dolar.obtener_precio_dolar('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
                    mensajeEnviar = {'instruccion': 'dolar', 'precio': precio[0]}

                elif "autogestion" in mensaje.lower():
                    if ManejoWEB.hayMensajesNuevos():
                        mensajeEnviar = {'instruccion': 'mensajeria', 'valor': 'si'}
                    else:
                        mensajeEnviar = {'instruccion': 'mensajeria', 'valor': 'no'}

                # TODO meter el tema de la alarma aca
                elif "alarma" in mensaje.lower() and ':' in mensaje.lower():
                    listaSeparada = mensaje.lower().split(' ')
                    tiempo = '0:0'
                    for a in listaSeparada:
                        if ':' in a:
                            tiempo = a
                    hora = tiempo.split(':')[0]
                    minutos = tiempo.split(':')[1]
                    mensajeEnviar = {'instruccion': 'undefined'}    # Ponemos undefined porque la alarma recien se va a mandar cuando llegue la hora
                    Alarma(int(hora), int(minutos))
                else:
                    mensajeEnviar= {'instruccion': 'unrecognized'}

                print("telefono: " + str(mensaje))
                print("arduino: " + str(mensajeEnviar))
                AdministradorArduino.retornarArduino().enviarMensaje(json.dumps(mensajeEnviar))


class AdministradorArduino:
    arduino = None

    @staticmethod
    def asignarArduino(arduino):
        AdministradorArduino.arduino = arduino

    @staticmethod
    def retornarArduino():
        return AdministradorArduino.arduino


class ClienteArduino(Thread):
    def __init__(self, socket, direccion):
        Thread.__init__(self)
        self.socket = socket
        self.direccion = direccion
        self.start()

    def run(self):
        print("El cliente se ha definido como arduino")
        while True:
            mensaje = self.socket.recv(10000).decode()
            if mensaje != "":
                print("Arduino:" + mensaje)

    def enviarMensaje(self, mensaje):
        self.socket.send(mensaje.encode())


class Alarma(Thread):
    def __init__(self, hora, minutos):
        print('Alarma establecida a las ' + str(hora) + ':' + str(minutos))
        # If todavia no paso
        ahora = time.localtime().tm_hour * 3600 + time.localtime().tm_min * 60
        hasta = hora * 3600 + minutos * 60

        segundos = hasta - ahora

        if segundos >= 0:
            print('Esperando ' + str(segundos) + ' segundos')
            time.sleep(segundos)

        else:
            print('Esperando ' + str(86400 - segundos) + ' segundos')
            time.sleep(86400 - segundos)

        AdministradorArduino.retornarArduino().enviarMensaje(json.dumps({'instruccion': 'alarma'}))
        print('Alarma enviada al Arduino.')
        time.sleep(86400)

direccionHost = "0.0.0.0"  # esto es porque es nuestro wifi local
puerto = 25000
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # esto inicia el servidor
serversocket.bind((direccionHost, puerto))  # el bind me prende el servidor
serversocket.listen(
    5)  # siempre se pone 5 ya que es la cola de conexión, o sea, cuantos dispositivos quedan en la cola de espera sin estar conectados

while True:
    cliente, direccionCliente = serversocket.accept()
    Cliente(cliente, direccionCliente)
