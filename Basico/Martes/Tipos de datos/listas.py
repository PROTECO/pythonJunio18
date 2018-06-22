# -*- coding: utf-8 -*-
############################
# Tipo de dato lista
############################

lista=[1,"Hola",10j,False,3.14,["Lista adentro de lista"]]
"""
listaVacia=[]
print("Lista de cosas: ", lista)
auxiliar=lista[0]
#Indexación
lista[0]="Hola"

print("Tipo de dato",type(lista))
print("Longitud",len(lista))

print("Búsqueda: ", "Hola" in lista)

#Operaciones
#El método append nos sirve para agregar elementos a una lista al final
listaVacia.append("Lo que sea")
listaVacia.append("menos")
listaVacia.append("eso")

print(listaVacia)
#El método pop nos sirve para quitar elementos de una lista, siempre son los últimos
listaVacia.pop()

print(listaVacia)
#El método insert nos permite agregar elementos en la posición deseada
listaVacia.insert(1,["Ya casi es el descanso xD"])

print(listaVacia)
#La palabra reservada del, nos permite eliminar elementos de la posición deseada
del listaVacia[0]
print(listaVacia)

vocales=["A","E","I","O","U"]

print("En orden: ",vocales)
#El método reverse nos permite invertir una lista
vocales.reverse()

print("Al revés",vocales)

numeros=[20,43,1,0,12,5]

print("Desordenados: ",numeros)
#El método sort nos permite ordenar distintos tipos de datos
numeros.sort()

print("Ordenados: ",numeros)

#El método index me regresa la posición en la que se encuentra el valor que le pasamos
print("Índice de 43: ",numeros.index(43))


print("Elementos de la lista que esta adentro de la otra lista: ",lista[5][0])

print("Comencemos :D")


nuevaLista=[1,2,5,5,6,7,7,7,7,8]
#El método count nos permite saber cuántas veces se repite un elemento

print("El elemento 7, se repite: ",nuevaLista.count(7)," veces")

###############################################################################

x=5
y=x

print("El valor de x es: ",x," y su id es: ",id(x))
print("El valor de y es: ",y," y su id es: ",id(y))
x=10
print("El valor de x es: ",x," y su id es: ",id(x))
print("El valor de y es: ",y," y su id es: ",id(y))


otraLista=lista

print("Lista original",lista," y su id es: ",id(lista))
print("Otra lista",otraLista," y su id es: ",id(otraLista))

lista[0]="Estoy siendo ingresado"


print("Lista original",lista," y su id es: ",id(lista))
print("Otra lista",otraLista," y su id es: ",id(otraLista))
#El método copy, nos permite crear una copia de una lista
"""
copiaLista=lista.copy()


lista[0]="Valor modificado"
print("Lista original",lista," y su id es: ",id(lista))
print("Otra lista",copiaLista," y su id es: ",id(copiaLista))

