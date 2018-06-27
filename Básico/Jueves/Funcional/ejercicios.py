#-*-coding:utf-8-*-
########################################
#Ejercicios 1 y 2
########################################

#Creamos una función para obtener los datos de una persona
def datos():
	datos=[]
	nombre=input("Ingresa tu nombre completo: ")
	datos.append(nombre)
	direc=input("Ingresa tu dirección")
	datos.append(direc)
	numTel=int(input("Ingresa tu número de télefono"))
	datos.append(numTel)
	numCta=int(input("Ingresa tu número de cuenta"))
	datos.append(numCta)
	return datos
#Otra función para darle formato a los datos que se ingresaron 
#en la función anterior

def formato(lista):
	print("Datos sin formato: ",lista,"\n\n")
	print("Datos con formato: ")

	for i in lista:
		print(lista.index(i),i)

datos_recibidos=datos()
#print(datos_recibidos)
formato(datos_recibidos)


#########################
#PROTECO Junio 2018-2
#########################