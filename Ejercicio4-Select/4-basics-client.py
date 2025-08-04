'''4. Servidor sin threads usando select
Usá una lista de sockets y select.select() para aceptar y leer múltiples clientes sin usar hilos.'''

import socket
import threading

def enviar_mensajes(cliente_socket):
    while True:
        mensaje = input()
        if mensaje.lower() == "salir":
            cliente_socket.send("Cliente desconectado".encode())
            cliente_socket.close()
            break
        if mensaje != '':
            try:
                cliente_socket.send(mensaje.encode())
            except:
                print("Error enviando mensaje")
                break
    
def recibir_mensaje(client_socket):
    while True:
        try:
            mensaje = client_socket.recv(1024).decode()

            if mensaje:
                print(f"El mensaje es {mensaje}")
            else:
                print("servidor desconectado")
                client_socket.close()
                break
        
        except:
            print("Error recibiendo mensaje o desconexion")
            client_socket.close()
            break
    

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = "127.0.0.1"
    PORT = 9000
    cliente.connect((IP, PORT))
    print("Conectado al servidor. Escribe mensajes (o 'salir' para desconectarte):")

    hilo_envio = threading.Thread(target=enviar_mensajes, args=(cliente,))
    hilo_recepcion = threading.Thread(target=recibir_mensaje, args=(cliente,))

    hilo_envio.start()
    hilo_recepcion.start()

if __name__ == "__main__":
    main()
