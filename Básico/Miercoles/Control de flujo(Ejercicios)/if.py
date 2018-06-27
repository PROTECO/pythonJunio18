palabra = input("Da una palabra: ")

# input nos regresa lo que escribe el usuario
# lo regresa como una cadena de caracteres

longitud = len(palabra)

# len nos da la longitud de una arreglo
# en este caso de la cadena de caracteres

if longitud < 5:
	print("Tiene menos de 5 letras")

if longitud > 5:
	print("Tiene mas de 5 letras")

if longitud == 5:
	print("Tiene 5 letras")