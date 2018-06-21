#########
#   Generadores
#########


# Un generador es un objeto que conforme lo vas llamando te devuelve una secuencia
# de valores, uno por uno, este guarda su estado cada vez para la proxima poder
# devolver el valor siguiente


# un generador se define igual que una funcion solo que se usa "yield" en vez de return
def generador():
    yield "hola"
    yield "siguiente"
    yield 1
    yield 2
    yield (3,3)

a=generador() #creamos un generador

print(a.__next__())#con __next__() accedmos al valor que sigue la secuencia
print(a.__next__())# Sintaxis de python2 next()
print(a.__next__())
print(a.__next__())
print(a.__next__())
# el generador se detiene en yield y cuando se vuelve a llamar continua donde se quedo


# ejemplo de generador mas complejo


# genera n numeros pares
def pares(n):
    a=0
    while n>0:   # mientras no acabemos los n numeros
        if a%2==0:    # si es par devuelvelo
            yield a
            n-=1
        a+=1

        
# podemos usar los generadores en un for in
for num in pares(5):
    print (num)


#Generador de numeros primos

def primos():
    prim=[]
    a=2.0
    while True:
        enc=False
        for n in prim:
            if a%n==0:
                enc=True
        if enc==False:
            prim.append(a)
            yield a
        a=a+1

a=primos()
cont=0
while ""==str(input("Presiona enter para el siguiente primo: ")):
    print ("Primo ",cont,": ",a.__next__(),sep="")
    cont+=1

#presiona una tecla diferente y despues enter para salir

# tambien los podemos generar como en las listas por compresion solo que con () en vez de []
gene=(x**2 for x in range(0,5))   # cuadrados de los numeros del 0 al 5

# list() nos permite convertir la secuencia completa de un generador en una lista

print (list(gene))