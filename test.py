import requests

url = 'https://criptoya.com/api/argenbtc/'
peticion = requests.get(url)

print(peticion.json())