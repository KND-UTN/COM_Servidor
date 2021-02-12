import requests


def obtener_clima(nombre_lugar):
    try:
        apiKey = "ba2362a43468ec964a38e3c79e60326b"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID" : apiKey, "q" : nombre_lugar, "units" : "metric", "lang" : "es"}
        respuesta = requests.get(URL, params = parametros)
        clima_final = respuesta.json()
        vector= respuesta_clima_final(clima_final)
        return vector
    except:
        print("Error. Intente nuevamente...")


def respuesta_clima_final(clima):
    try:
        temperatura = str(int(clima["main"]["temp"]))
        humedad = str(int(clima["main"]["humidity"]))
        vector = [temperatura,humedad]
        return vector
    except:
        print("Ha ocurrido un error, intente nuevamente")


if __name__ == "__main__":
    nombre_lugar = "Córdoba, arg"
    print(obtener_clima(nombre_lugar))
