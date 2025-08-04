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
#Server

import socket
import threading

# 1. El servidor crea su socket propio
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. El servidor vincula su socket a la dirección IP y puerto deseado (localhost)
direccion_ip = "127.0.0.1"
port = 8000
server.bind((direccion_ip, port))

# 3. El servidor se pone en modo escucha para aceptar conexiones (listen)
server.listen()
print("Servidor escuchando")

    #Def manejar_clientes
        # 8. El servidor recibe data (mensaje) por parte del cliente dentro de un bucle
        # 9. El servidor procesa o muestra el mensaje recibido
        # 10. (Opcional) El servidor envía respuesta al cliente   
        # 11. Si el cliente se desconecta, el servidor cierra la conexión con ese cliente
        # 13. El servidor sigue aceptando otros clientes en paralelo con threads
def manejar_cliente(cliente, adrr):
    print(f"Conexion establecida con {adrr}")
    while True:
        try:
            mensaje = cliente.recv(1024).decode()
            if not mensaje:
                break

            print(f"Mensaje de {adrr}: {mensaje}")
            respuesta = f"Mensaje recibido: {mensaje}"
            cliente.send(respuesta.encode())

        except:
            break
    
    print(f"Cliente {adrr} desconectado")
    cliente.close()

# 4. El servidor espera conexiones dentro de un bucle infinito
def aceptar_conecciones():
    while True:
        cliente, adrr = server.accept()
        hilo_cliente = threading.Thread(target=manejar_cliente, args=((cliente, adrr))) 
        hilo_cliente.start()
    
    
aceptar_conecciones()

