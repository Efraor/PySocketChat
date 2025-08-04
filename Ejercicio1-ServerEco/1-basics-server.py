# Importar la libreria socket para poder utilizarlo
## DESDE EL SERVIDOR
# 1. El servidor crea su socket propio
# 2. El servidor vincula su socket a la direccion IP y puerto que desea (localhost)
# 3. El servidor escucha, osea espera por conexiones
# 4. El servidor acepta conexiones
# 8. El servidor recibe data (mensaje) por parte del cliente
# 9. El servidor envia data al cliente
# 12. El servidor recibe el mensaje de cierre del cliente
# 13. El servidor cierra su conexion
########################
## DESDE EL CLIENTE
# 5. El cliente crea su propio socket
# 6. El cliente conecta su socket a la misma direccion IP y puerto colocado en el servidor (se establece conexion)
# 7. El cliente envia data (mensaje)
# 10. El cliente recibe data del servidor
# 11. El cliente decide cerrar conexion

#------------------------------------------------------------------------------------------------------------------------#
#server
import socket

# 1. El servidor crea su socket propio
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. El servidor vincula su socket a la direccion IP y puerto que desea (localhost)
direccion_ip = "127.0.0.1"
port = 8000
server.bind((direccion_ip,port))

# 3. El servidor escucha, osea espera por conexiones
server.listen()

# 4. El servidor acepta conexiones
cliente, addr = server.accept()
print(f"Conectado a {addr[0]}:{addr[1]}")

# 8. El servidor recibe data (mensaje) por parte del cliente
mensaje_1 = cliente.recv(1024).decode()
print(f"El mensaje_1 es: {mensaje_1}")

# 9. El servidor envia data al cliente
cliente.send(mensaje_1.encode())

# 12. El servidor recibe el mensaje de cierre del cliente
mensaje_2 = cliente.recv(1024).decode()
print("cerrando cliente")
cliente.close()

# 13. El servidor cierra su conexion
print("Cerrando conexion del servidor")
server.close()
