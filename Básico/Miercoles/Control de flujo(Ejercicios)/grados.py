#Convertir grados centigrados a fahrenheit

print("1: F -> C")
print("2: C -> F")
eleccion = input("Escoge el tipo de conversión: ")

grados = float(input("Ingresa los grados a convertir: "))

if eleccion == "1":
	gradosn = (grados - 32)*(5/9)
	print("%.3f Celsius" % gradosn)
elif eleccion == "2":
	gradosn = (9/5)*grados + 32
	print("%.3f Fahrenheit" % gradosn)
else:
	print("Opción no valida")