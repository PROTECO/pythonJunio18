# -*- coding: utf-8 -*-
############################
# Tipo de dato conjunto(Sets)
############################


conjunto={1,2,3,4,5,10}

print("El conjunto pertenece a la clase: ",type(conjunto))

print(conjunto)
lista=[1,2,4,6,8]

conjunto2=set(lista)

print(conjunto2)

conjunto3={True,2,40,"Hola"}
print(conjunto3)
conjunto3.add(False)
conjunto3.add(2)
conjunto3.add("ke ase?")
print(conjunto3)
#No soporta indexación
#print("Indexación: ",conjunto3[0])

#Operaciones

print("Diferencia: ",conjunto-conjunto2)
print("Diferencia simétrica: ",conjunto^conjunto2)
print("Union: ",conjunto|conjunto2)
print("Intersección: ",conjunto2&conjunto)

###########
#Frozensets
###########

conjuntoF=frozenset([True,24,"Ya casi son 4:30",":("])
print("Conjunto congelado: ",conjuntoF)

conjuntoF.add("Agregame")
print(conjuntoF)