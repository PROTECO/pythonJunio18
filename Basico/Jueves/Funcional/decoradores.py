#############
# Decoradores
#############

# Son funciones que reciben una funcion como parametro y regresa otra funcion
# esta otra funcion (funcion decorada) hace lo mismo que la primera pero
# con funcionalidad nueva


# decorador que agrega un mensaje con el nombre de la funcion
def nombre(funcion):
    def decorada(*parms):    # * se usa para indicar que la funcion puede tener 0 o mas parametros
        # acciones nuevas de la funcion
        print("Se ha iniciado la funcion %s"%(funcion.__name__))
        return funcion(*parms)  #funcion original
    return decorada


def cubo(n):
    print (n**3)

@nombre         # se puede indicar el decorador usando @ para que se llame solo
def suma(a,b):
    print (a+b)



F=nombre(cubo)    # sin usar @
F(2)

suma(3,7)         # usando @


# decorador que quita numeros repetidos de una lista que nos regrese una funcion
def quitaRepetido(funcion):
    def funDecorada(*parms):
        print ("Decorador quitaRepetido:")
        lista=funcion(*parms)
        print("Lista original: ",lista)
        nueva=[]
        for valor in lista:
            n=True
            for repeticion in nueva:
                if repeticion==valor:
                    n=False
            if n==True:
                nueva.append(valor)
        print("Lista sin valores repetidos: ",nueva)
        print("")
    return funDecorada


@quitaRepetido
def sumaListas(li,li2):   # suma los elementos de dos listas
    return map(lambda a,b: a+b,li,li2)

@quitaRepetido   #podemos decorar con mas de un decorador
@nombre          #primero se decora con el de arriba y sigue hacia abajo
def dobles():
    return [1,1,2,2,3,3,4,5,6,7,4,4]


dobles()
a=[1,2,1,2,1,2,1,2]
b=[3,2,3,2,3,2,3,2]
sumaListas(a,b)



#Funcion map
#a cada uno de los elementos de la lista
#le aplica la funcion que le pasemos
#devuelve una lista

def cuadrado(n):
    return n*n

lista=[1,2,3,4]

for x in lista:
    print(cuadrado(x))


print(list(map(cuadrado,lista)))

