import requests

def obtener_precio_dolar(URL):
    respuesta = requests.get(URL)
    precio = respuesta.json()
    venta = str(precio[0]["casa"]["venta"])
    venta = str(int(float(venta.replace(",","."))))
    vector = [venta]
    return vector

#URL = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
#print(obtener_precio_dolar(URL))
