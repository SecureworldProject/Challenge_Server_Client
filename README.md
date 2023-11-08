# Challenge_Server_Client

Cliente para el challenge de servidor

Ejempo configuracion json
```json
{
	"FileName": "client_server_challenge.dll",
	"Description": "Challenge that connects against a server and retrieves a key depending on the sent parameters",
	"Props": {
		"validity_time": 3600,
		"refresh_time": 3000
	},
	"Requirements": "none"
}
```

## Funcionamiento

El challenge dispone de dos partes diferenciadas. Por un lado, el cliente requiere de las librerías:
- socket: permite abrir un socket de comunicación
- random: permite generar números aleatorios
- requests: permite realizar llamadas HTTP

En el lado del cliente, toda la funcionalidad se encuentra dentro de la función executeChallenge(), dentro del fichero client.py.
Es necesario mandarle al servidor tres parámetros:
- reading_id: un número que identifica una lectura en concreto. Para la prueba de concepto esto se hace mediante un random entre  0-100.
- ip: en este caso se le envía la dirección 8.8.8.8. El módulo socket se utiliza para conectar con esta dirección IP.
- data: un número de tamaño indefinido que simula un dato de entrada al challenge. En este caso se ha enviado el número '1023'.
Esta información se envía al servidor empleando el módulo requests mediante un método HTTP POST.

