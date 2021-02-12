import threading
import time

class Alarma(threading.Thread):
    def wait_until(self, hora, minutos):
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

        print('RIIIIING')
        time.sleep(86400)


if __name__ == "__main__":
    alarma = Alarma()
    alarma.wait_until(19, 12)
