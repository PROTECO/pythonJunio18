# Contar el numero de vocales de frase

frase = """
Yo soy el aventurero
El mundo me importa poco
Cuando una mujer me gusta
Me gusta a pesar de todo
"""

numero = 0

for caracter in frase:
	if caracter in ("a","e","i","o","u"):
		numero += 1

print(numero)