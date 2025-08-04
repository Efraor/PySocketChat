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
#cliente
import socket

# 5. El cliente crea su propio socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 6. El cliente conecta su socket a la misma direccion IP y puerto colocado en el servidor (se establece conexion)
direccion_ip = "127.0.0.1"
port = 8000
cliente.connect((direccion_ip, port))

# 7. El cliente envia data (mensaje)

cliente.send("Hola sock".encode())

# 10. El cliente recibe data del servidor
mensaje = cliente.recv(1024).decode()
print(f"Eco del servidor: {mensaje}")

# 11. El cliente decide cerrar conexion
cliente.send("Cerrando conexion".encode())
print("Cerrando conexion")
cliente.close()

