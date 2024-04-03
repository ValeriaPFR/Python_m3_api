import requests

#función que obtiene datos de la api y las retorna en formato JSON.
def obtener_datos():
    url = 'https://aves.ninjas.cl/api/birds'
    response = requests.get(url)
    return response.json()