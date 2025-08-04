# INICIO

# 1. Importar librería socket y threading

# 2. Crear socket cliente

# 3. Conectar socket al servidor (IP y puerto)

# 4. Definir función para recibir mensajes del servidor:
#     a. Bucle infinito:
#         i. Recibir datos del servidor
#         ii. Si no recibe datos, cerrar conexión y salir del bucle
#         iii. Mostrar mensaje recibido en consola

# 5. Crear un hilo para ejecutar la función que recibe mensajes del servidor

# 6. Bucle infinito en el hilo principal para enviar mensajes:
#     a. Leer entrada del usuario (mensaje)
#     b. Enviar mensaje al servidor
#     c. Si el mensaje es "salir" o equivalente, cerrar conexión y salir del bucle

# 7. Cerrar socket cliente

# FIN

import socket
import threading


def recibir_mensajes_sevidor(cliente_socket):
    while True:
        try:
            msg_server = cliente_socket.recv(1024).decode()
            if not msg_server:
                print("Desconectando del servidor")
                break
            print(f"\n{msg_server}")
        except:
            print("Error al recibir el mensaje. Desconectado")
            break
    cliente_socket.close()

def main():
    
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_server = "127.0.0.1"
    port = 8000

    try:
        cliente.connect((ip_server, port))
        print("conectado al servidor ")

    except:
        print("No se puedo conectar al servidor")
        return
    
    hilo_recibir = threading.Thread(target=recibir_mensajes_sevidor, args=((cliente,)))
    hilo_recibir.start()

    while True:
        print("escribe un mensaje o salir para desconectarse del servidor")
        mensaje = input("escribe un mensaje: " )
        if mensaje.lower() == "salir":
            cliente.send("El cliente se desconecto".encode())
            break
        cliente.send(mensaje.encode())

    cliente.close()
    print("Desconectando del servidor")

if __name__ == "__main__":
    main()

