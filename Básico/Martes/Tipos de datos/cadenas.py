# -*- coding: utf-8 -*-
############################
# Tipo de dato cadena
############################

cadena="Hola"
cadena2="mundo"

cadenaLargas="""
Esta es una cadena larga, y puede incluir
saltos de línea
como 
estos
"""

print(cadena,cadena2)

print(cadenaLargas)

cadenaVacia=""

print(cadenaVacia)

#Se utiliza una r al inicio de una cadena para indicar que es una cadena cruda
cadenaCruda=r"Esta es una cadena cruda, no esta cocida \n\n\n"
print(cadenaCruda)
print("Clase de las cadenas: ", type(cadena))

print("Indexación: ", cadena[0])
print("Indexación: ", cadena[1])
print("Indexación: ", cadena[2])
print("Indexación: ", cadena[3])

print("Indexación",cadena2[-1])
print("Indexación",cadena2[-2])
print("Indexación",cadena2[-3])
print("Indexación",cadena2[-4])
print("Indexación",cadena2[-5])

print("El tamaño de la cadena es ",len(cadena))

trabalenguas="parangaricutimrimicuaro"

print("Tamaño: ",len(trabalenguas))
#La asignación no esta permitida porque las cadenas son inmutables
trabalenguas[0]="z"

print(trabalenguas)
