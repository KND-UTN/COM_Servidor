__author__ = "Ignacio Pieve Roiger & Leila Aylen Spini"
__version__ = "0.2"

# Este modulo va a ir abriendo todas las regularidades periodicamente, entrando a sus paginas y
# comparará si los registros anteriores coinciden.
# Caso contrario, se enviara una notificacion por con el modulo de Notificaciones.

import AccesoBD as bd
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import pathlib #retorna la ubicacion del archivo

from selenium.webdriver.chrome.options import Options


def getUsuario():
    try:
        return bd.leer('SELECT usuario FROM Usuario')[0][0]
    except:
        return False


def getClave():
    try:
        return bd.leer('SELECT clave FROM Usuario')[0][0]
    except:
        return False


def registrarUsuario(usuario, clave):
    bd.ejecutar('DELETE FROM Usuario;')
    bd.ejecutar('INSERT INTO Usuario (usuario, clave) VALUES ("' + usuario + '", "' + clave + '");')


def hayMensajesNuevos():
    while True:
        chrome_options = Options()
        #chrome_options.add_argument("--headless") #para que la pagina se abra a escondidas
        chrome_options.add_argument("--log-level=3")
        driver = wd.Chrome(executable_path=(str(pathlib.Path(__file__).parent.absolute()) + '\\chromedriver.exe'), chrome_options=chrome_options)
        abrirAutogestion(driver)
        mensajes_actualizados = obtener_mensajeria(driver)
        mensajes_nuevos = encontrar_mensajes_nuevos(mensajes_actualizados)

        if mensajes_nuevos != []:
            return True
        return False


def abrirAutogestion(driver):
    driver.get('https://www.frc.utn.edu.ar/logon.frc') #abre autogestion

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtUsuario"))) #no hagas nada hasta que exista txtUsuario

    driver.find_element_by_id('txtUsuario').send_keys(getUsuario())
    Select(driver.find_element_by_id('txtDominios')).select_by_visible_text('sistemas')
    driver.find_element_by_id('pwdClave').send_keys(getClave())
    driver.find_element_by_id('btnEnviar').click()

    time.sleep(1)


def obtener_mensajeria(driver):
    # Entramos a autogestion (El driver ya tiene que estar logueado) y esperamos 4 segundos a que se carge el JS
    driver.get('https://www.frc.utn.edu.ar/academico3/')
    time.sleep(4)

    # Buscamos el iFrame de mensajeria
    frame_mensajeria = driver.\
        find_element_by_class_name('dhx_tabcontent_zone').\
        find_elements_by_class_name('dhx_tabcontent_sub_zone')[1].\
        find_element_by_tag_name('iFrame')

    # Hacemos que el driver cambie al contexto del iFrame (Nuevo codigo HTML, pagina distinta)
    driver.switch_to.frame(frame_mensajeria)

    # Obtenemos los mensajes
    mensajes = driver.find_element_by_class_name('tab-page').text

    # Uno por uno los vamos metiendo raw en una lista y retornamos la lista
    lista_formateada = []
    for a in mensajes.split('\n\n'):
        lista_formateada.append(formatear_mensaje_raw(a))
    return lista_formateada


def formatear_mensaje_raw(mensaje):
    # Aca entra un mensaje (NO la lista, solo el mensaje), lo formatea y retorna
    partes = mensaje.split('\n')

    curso = (partes[0].split('-Publicado')[0]).split('  ')[1]
    fecha = (partes[0].split('-Publicado: ')[1]).split(',')[0]
    profesor = partes[0].split(fecha + ', ')[1]
    msg = partes[1]

    return [curso, fecha, profesor, msg]


def encontrar_mensajes_nuevos(lista_actualizada):
    mensajesNuevos = []
    for a in lista_actualizada:
        consulta = bd.leer_parametros('SELECT * FROM Mensajes WHERE fecha=? AND curso=? AND profesor=? AND mensaje=?', (a[1], a[0], a[2], a[3], ))
        if consulta == []:
            mensajesNuevos.append(a)
            print('Mensaje nuevo encontrado, insertando...')
            print('Datos del mensaje encontrado: fecha{' + a[1] + '}, curso{' + a[0] + '} profesor{' + a[2] + '}')

            bd.ejecutar_parametros('INSERT INTO Mensajes (fecha, curso, profesor, mensaje) VALUES (?,?,?,?)', (a[1], a[0], a[2], a[3], ))

            print('Insertado con exito\n')
    return mensajesNuevos


if __name__ == '__main__':
    # Con esta linea registramos el usuario nuevo y la clave
    # registrarUsuario('usuario', 'clave')
    if getUsuario() is False:
        input('No hay usuarios registrados o no se ha cargado el token de slack.' +
              '\nRegistre los datos con el modulo main y vuelva a intentarlo.')
        exit()
    print(hayMensajesNuevos())