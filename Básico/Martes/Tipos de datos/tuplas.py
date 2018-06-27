# -*- coding: utf-8 -*-
############################
# Tipo de dato tupla
############################

tupla=("Hola",1,2,3,[1,2,3])
tupla2=("contraseña",1234)
print("La tupla viene de la clase: ", type(tupla))
print("Indexación: ",tupla[2])
print("Longitud: ",len(tupla))
print("Concatenación: ",tupla+tupla2)

#Las tuplas no permiten su modificación, porque son inmutables
#tupla2[1]="Asignacion"

tupla[4][2]=8

print(tupla)
