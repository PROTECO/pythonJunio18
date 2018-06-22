# iteracón for en una lista

numeros = [8,3,6,2]
for num in numeros:
  print(num - 1)
  
# iteración for en una tupla

dias = ("lunes","martes","miercoles","jueves","viernes","sabado","domingo")

for dia in dias:
  if dia == "martes":
    print("hoy es",dia)
  else:
    print("hoy no es",dia)

# iteración for en un diccionario

diccionario = {"paco":9,"jorge":10,"luis":7}

for llave in diccionario:
  print(llave,"sacó",diccionario[llave])

# iteración for con desempaquetado

coloresFav = [("Vanesa","morado"),("Andres","verde"),("Jessica","rojo"),("Miguel","azul")]

for nombre,color in coloresFav:
  print("El color",color,"es el favorito de",nombre)

# iteración for en una cadena de texto

for letra in "Cadena de texto":
	print(letra+"-")
