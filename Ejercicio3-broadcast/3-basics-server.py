# INICIO

# 1. Importar librerías necesarias
#     - socket
#     - threading

# 2. Crear lista global para almacenar los sockets de todos los clientes conectados

# 3. Definir función manejar_cliente(cliente_socket, direccion_cliente):
#     a. Agregar cliente_socket a la lista global de clientes
#     b. Mostrar mensaje de conexión establecida con direccion_cliente
#     c. Bucle infinito:
#         i. Intentar recibir datos del cliente
#         ii. Si no recibe datos, salir del bucle (cliente desconectado)
#         iii. Mostrar el mensaje recibido
#         iv. Reenviar (broadcast) el mensaje recibido a todos los clientes en la lista excepto al que lo envió
#     d. Eliminar cliente_socket de la lista global de clientes
#     e. Cerrar cliente_socket
#     f. Mostrar mensaje de desconexión del cliente

# 4. Crear socket del servidor

# 5. Configurar dirección IP y puerto

# 6. Asociar (bind) el socket a la IP y puerto

# 7. Poner el socket en modo escucha (listen)

# 8. Mostrar mensaje de que el servidor está esperando conexiones

# 9. Bucle infinito para aceptar nuevos clientes:
#     a. Aceptar conexión entrante (cliente_socket, direccion_cliente)
#     b. Crear un nuevo hilo (thread) para manejar a ese cliente
#     c. Iniciar el hilo

# FIN



#--------------------------------------------------------------------------------------------------------------#

import socket
import threading

clientes = []

def manejar_clientes(cliente_socket, drrs_cliente):
    clientes.append(cliente_socket)
    print(f"Conexion establecida con: {drrs_cliente}")

    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode()
            if not mensaje:
                break
            
            print(f"Mensaje de {drrs_cliente}: {mensaje}")
            
            for cliente in clientes:
                if cliente != cliente_socket:
                    cliente.send(f"{drrs_cliente} :{mensaje}".encode())

        except:
            break
    
    print(f"Cliente desconectado: {drrs_cliente}")
    clientes.remove(cliente_socket)
    cliente_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_server = "127.0.0.1"
    port = 8000
    server.bind((ip_server, port))
    server.listen()
    print("Servidor escuchando")

    while True:
        cliente, adrrs = server.accept()
        hilo_cliente = threading.Thread(target=manejar_clientes, args=((cliente, adrrs)))
        hilo_cliente.start()

main()