peso = float(input("Dame tu peso en kilogramos: "))
estatura = float(input("Dame tu estatura en metros: "))

# utilizamos float() para convertir
# la entrada a un número con decimales(flotante)

imc = peso/estatura**2

if imc < 18.5:
	print("Bajo de peso")
elif imc < 24.9:
	print("Normal")
elif imc < 29.9:
	print("Sobrepeso")
elif imc < 34.9:
	print("Obesidad")
else:
	print("Obesidad 2")