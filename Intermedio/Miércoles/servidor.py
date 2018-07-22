# Servidor

import socket

ss=socket.socket()
#Para poder hacer la conexion entre dos equipos cambiar la ip
#de "localhost" al formato "192.168.1.x", recuerden que pueden
#saber su ip con el comando "ipconfig" en Windows e "ifconfig"
#en linux o Mac, también deben cambiarla en el otro programa

#ip = input("Ingresa tu dirección IP: ")
#puerto = int(input("Ingresa tu puerto :"))
#
ss.bind(("localhost",9000))

ss.listen(1)

conn,addr=ss.accept()

print("Iniciando Servidor!!")
print("Cliente conectado desde: ",addr[0],":",addr[1])

while True:
	recibido=conn.recv(5000).decode()
	
	if recibido=="adios":
		break
	print("Cliente dice: ",recibido)
	conn.send(input("Ingresa tu mensaje: ").encode())
	
print("Se ha terminado la conexion")
#Recordar que es muy importante cerrar explicitamente la conexion
ss.close()