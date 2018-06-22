from functools import reduce
#################
#   Lambdas y funciones de orden superior
#################

# se usan para crear funciones en linea, sin nombre que se usaran en el momento
# tambien llamadas funciones anonimas , se usan en el momento

# se construyen mediante el operador lambda

# las funciones lambda estan limitadas a una sola expresion
funcion=(lambda a,b:a+b) #argumentos separados por comas ":" lo que regresa 

print(funcion(3,3))

# map() aplica una funcion a cada elemento de una secuencia y nos crea una
# nueva lista con los valores devuelto por la funcion

li=[1,2,3,4,5,6,7,8]

li2= map(lambda n: n**2,li)          # usando lambda ponemos una funcion que eleva al cuadrado

print(list(li2))


# ahora exactamente lo mismo pero con una funcion normal

def cuadrado(a):
    return a**2

li2=map(cuadrado,li)

print(list(li2))



# filter() hace lo mismo que map solo que la funcion debe ser verdadera o falsa
# si es falsa, no añade el valor a la nueva lista

li2=filter(lambda n: n%4==0,li)   # multiplos de 4

print(list(li2))


# reduce() aplica la funcion a dos elementos de la lista, los remueve y añade el
# valor obtenido por la funcion, sigue asi hasta que haya un solo valor
otraLista=[0,1,2,3,4,5,6,7,8,9]

lista2 = reduce(lambda a,b:a+b,otraLista)  # suma todos los elementos de li

print(lista2)