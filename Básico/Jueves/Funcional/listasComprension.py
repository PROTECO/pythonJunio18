#########
#   Listas por compresion
#########

# es una caracteristica de python que permite crear listas a partir de
# otras listas bajo ciertos criterios

# se construyen con una expresion que modifica el elemento original y algunos
# for e if para determinar como crear la nueva lista


li=[1,2,3,4,5,6,7,8]    #una lista

nli= [n+2 for n in li]   #lista por compresion
# aqui se hace justamente lo que se lee: a n sumale 2 por cada n en la lista li
        # nos resulta una lista donde a todos los valores se les sumo 2
        
print (nli)

nli= [n/2 for n in li]   # la mitad de cada elemento de li
print (nli)

# podemos colocar mas de un for en su contruccion

li2=[1,2,3]

nli= [n*a for n in li for a in li2]  # multiplica cada elemto de li por cada elemento de li2
# funcionan como for anidados uno dentro de otro siendo el de mas a la derecha
# el mas interior y el de la izquierda el mas exterior
print (nli)

# despues de los for puedemos colocar uno o mas if

nli=[n/2 for n in li if n%2==0]
# obtenemos una lista con solo las mitades de los numeros pares
print (nli)