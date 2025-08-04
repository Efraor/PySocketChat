'''4. Servidor sin threads usando select
Usá una lista de sockets y select.select() para aceptar y leer múltiples clientes sin usar hilos.'''

import socket
import select

IP = "127.0.0.1"
PORT = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

sockets_activos = [server_socket] # Lista de sockets que vamos a monitorear

print("servidor activo")
print(f"Servidor escuchando en {IP}:{PORT}")

while True:
    # select.select monitorea sockets listos para leer, escribir o con error
    sockets_para_leer, _, _= select.select(sockets_activos, [], [])

    for sock in sockets_para_leer:
        if sock == server_socket:
            cliente_socket, adrr = server_socket.accept()
            sockets_activos.append(cliente_socket)
            print(f"Nuevo cliente conectado desde {adrr}")

        else:
            try:
                mensaje = sock.recv(1024).decode()
                if mensaje:
                    print(f"Mensaje recibido: {mensaje}")
                    for cliente in sockets_activos:
                        if cliente != server_socket and cliente != sock:
                            try:
                                cliente.send(mensaje.encode())
                            except:
                                cliente.close()
                                sockets_activos.remove(cliente)

                else:
                    print("cliente desconectado")
                    cliente.close()
                    sockets_activos.remove(cliente)


            except:
                print("Error o cliente desconectado")
                sock.close()
                sockets_activos.remove(sock)


