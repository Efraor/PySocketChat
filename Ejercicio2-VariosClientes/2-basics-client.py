# Importar las librerías necesarias: socket y threading

########################
## DESDE EL SERVIDOR (MULTICLIENTE CON THREADS)
# 1. El servidor crea su socket propio
# 2. El servidor vincula su socket a la dirección IP y puerto deseado (localhost)
# 3. El servidor se pone en modo escucha para aceptar conexiones (listen)
# 4. El servidor espera conexiones dentro de un bucle infinito
# 5. Cuando un cliente intenta conectarse, el servidor acepta la conexión
# 6. El servidor crea un nuevo hilo (thread) para manejar a ese cliente
# 7. El hilo ejecuta una función donde:
    # 8. El servidor recibe data (mensaje) por parte del cliente dentro de un bucle
    # 9. El servidor procesa o muestra el mensaje recibido
    # 10. (Opcional) El servidor envía respuesta al cliente
    # 11. Si el cliente se desconecta, el servidor cierra la conexión con ese cliente
# 12. El hilo termina cuando el cliente cierra la conexión
# 13. El servidor sigue aceptando otros clientes en paralelo con threads

########################
## DESDE EL CLIENTE (MULTICLIENTE)
# 1. El cliente crea su propio socket
# 2. El cliente conecta su socket a la dirección IP y puerto del servidor (se establece la conexión)
# 3. El cliente envía un mensaje al servidor
# 4. (Opcional) El cliente recibe respuesta del servidor
# 5. El cliente puede seguir enviando mensajes dentro de un bucle
# 6. Cuando el cliente decide, envía un mensaje de cierre o simplemente cierra la conexión
# 7. El cliente cierra su socket


#---------------------------------------------------------------------------------------------------#
#Cliente
import socket

# 1. El cliente crea su propio socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. El cliente conecta su socket a la dirección IP y puerto del servidor (se establece la conexión)
direccion_ip = "127.0.0.1"
port = 8000
cliente.connect((direccion_ip, port))
print("Conectando con el servidor")

# 3. El cliente envía un mensaje al servidor
while True:
    msg = input("Ingrese el mensaje o escribe 'salir' para cerrar la conexión.")
    cliente.send(msg.encode())

    if msg.lower() == "salir":
        break

# 4. (Opcional) El cliente recibe respuesta del servidor
# 5. El cliente puede seguir enviando mensajes dentro de un bucle
    respuesta = cliente.recv(1024).decode()
    print(f"respuesta del servidor: {respuesta}")


# 6. Cuando el cliente decide, envía un mensaje de cierre o simplemente cierra la conexión
# 7. El cliente cierra su socket
cliente.close()
print("conexion cerrada")





