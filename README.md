# Ev-global-m3-Python-API
 Se solicita generar un prototipo muy sencillo en el cual se puedan observar algunas imágenes de pájaros típicos de Chile junto con su nombre en español e inglés. La idea es que esta información pueda ser eventualmente transformada en señaléticas bilingües que permitan fomentar el turismo en Chile. 

Funcionalidades:

Llamado a la API: Se realiza un llamado a la API 'https://aves.ninjas.cl/api/birds' para obtener la información necesaria.

Templates HTML: Se han creado templates HTML para mostrar la información de las aves.

Exportación a HTML: El sitio web se exporta como un archivo HTML que puede ser abierto en el navegador.

Modularización:

El código se ha modularizado en 3 archivos , por un lado el archivo obtener_datos_aves.py para obtener los datos desde la api y retornar desde una función en formato JSON, el archivo html_template.py, que estructura la plantilla del html y el archivo main.py que es la estructura principal del programa y llama los archivos anteriores. 