# -*- coding: utf-8 -*-
############################
# Tipo de dato diccionario
############################

#Formato del diccionario diccionario={llave:valor}
#LLave debe ser inmutable, y valor puede ser cualquiera1
diccionario={"Jorge":"1234","Julio":1765675,"Gali":2543,"Luis":True,"Aldo":[1,2,4]}

print("La contraseña de Jorge es: ",diccionario["Jorge"])
print("La contraseña de Julio es: ",diccionario["Julio"])
print("La contraseña de Gali es: ",diccionario["Gali"])
print("La contraseña de Aldo es: ",diccionario["Aldo"])


calificaciones={"Jorge":10,"Gali":9,"Aldo":6,"Julio":8,"Luis":"NP"}

print("Calificación de Jorge: ", calificaciones["Jorge"])
print("Calificación de Jorge: ",calificaciones.get("Jorge"))

#Modificar un valor

calificaciones["Jorge"]=8 

print("Calificación de Jorge: ", calificaciones["Jorge"])
#El método values me devuelve los valores de todas las llaves del diccionario
print(calificaciones.values())
#El método ítems me devuelve un diccionario que contiene en tuplas la llave y el valor
print(calificaciones.items())	
