numero = int(input("Dame un número: "))
# Necesitamos usar int() para convertir
# lo que obtenemos del usario a un entero

# % -> operador modulo
# regresa el residuo de una divición

if numero%2 == 0:
	print('Es un número par')
else:
	print('Es un número impar')