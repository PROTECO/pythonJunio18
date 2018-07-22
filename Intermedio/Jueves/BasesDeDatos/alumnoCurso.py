#################################
#Bases de datos
#################################

import sqlite3
import os
conn=sqlite3.connect('cursosProteco.db')  #Hacemos la conexión a la base de datos
#Y la crea

#La mayoría de las operaciones sobre las bases de datos se hacen utilizando
#un objeto que apunta a la base de datos y a través del cual podemos 
#ejecutar instrucciones similares al SQL estandar para obtener, insertar, actualizar o
#borrar algun dato.

cursor=conn.cursor()

print("\n\t\tBase de datos de los cursos de PROTECO")


#Creación de tablas
#Las operaciones se ejecutan a través del método execute del curso que
#declaramos

try:
	cursor.execute('''
		CREATE TABLE alumno(
		folio INTEGER PRIMARY KEY,
		nombreAlu TEXT,
		apPat TEXT, 
		apMat TEXT)''')
	cursor.execute('''
		CREATE TABLE curso(
		idCurso INTEGER PRIMARY KEY,
		nombreCurso TEXT,
		cupo INTEGER)''')
	cursor.execute('''
		CREATE TABLE alumno_curso(
		folio INTEGER,
		idCurso INTEGER,
		calificacion FLOAT,
		FOREIGN KEY(folio) REFERENCES alumno(folio)
		FOREIGN KEY(idCurso) REFERENCES curso(idCurso)
		PRIMARY KEY(folio,idCurso)
		)''')
	
except:
	print("Saltándose la creación de la tabla porque ya existe! :D")

#Insertar cosas.
"""La forma recomendada es utilizar placeholders(marcadores de posición)
puesto que si armamos la cadena usando variables de python podemos correr
el riesgo de que nos hagan SQL injection"""



while True:
	opcion = input(""" 
					  \n1.-Registrar alumno
					  \n2.-Registrar curso
					  \n3.-Ver cursos
					  \n4.-Ver alumnos
					  \n5.-Inscribir curso
					  \n6.-Eliminar curso
					  \n7.-Eliminar alumno
					  \n8.-Actualizar datos alumno
					  \n9.-Actualizar datos curso
					  \n10.-Asignar/Cambiar calificación
					  \n11.-Salir \t\tIngresa la opción que deseas realizar:""")
	if opcion=='1':
		#Solicitamos los datos a guardar
		folio = int(input("Ingresa el folio del asistente: "))
		nombreAlu = input("Ingresa el nombre: ")
		apPat = input("Ingresa el apellido paterno: ")
		apMat = input("Ingresa el apellido m""aterno: ")
		
		#Query a ejecutar
		cursor.execute('INSERT INTO alumno(folio,nombreAlu,apPat,apMat) VALUES("%d", "%s","%s","%s")'%(folio,nombreAlu,apPat,apMat))	
		#Recordar que hay que guardar los cambios
		conn.commit()
		print("Alumno agregado exitosamente!")
	elif opcion=='2':
		#Solicitamos los datos
		idCurso = int(input("Ingresa el id del curso: "))
		nombreCurso = input("Ingresa el nombre del curso: ")
		cupo = int(input("Ingresa el cupo del curso: "))
		#Query a ejecutar
		cursor.execute('INSERT INTO curso(idCurso,nombreCurso,cupo) VALUES("%d", "%s","%d")'%(idCurso,nombreCurso,cupo))	
		print("Curso agregado exitosamente!")
		#Salvar cambios	
		conn.commit()	
		
	elif opcion=='3':
		for row in conn.execute('SELECT * FROM curso ORDER BY idCurso ASC'):
			print("id curso: ",row[0]," Nombre curso: ",row[1],"Cupo: ",row[2])

	elif opcion=='4':
		for row in conn.execute('SELECT * FROM alumno ORDER BY folio DESC'):
			print("Folio: ",row[0]," Nombre: ",row[1],row[2],row[3])
	
	elif opcion=='5':
		os.system("clear")
		print("Cursos disponibles: \n")
		for row in conn.execute('SELECT * FROM curso ORDER BY idCurso ASC'):
			print("id curso: ",row[0]," Nombre curso: ",row[1],"Cupo: ",row[2])		
		folio = int(input("Ingresa tu folio: "))
		idCurso = int(input("Ingresa el id del curso a inscribir: "))
		cursor.execute('INSERT INTO alumno_curso(folio,idCurso) VALUES("%d", "%d")'%(folio,idCurso))	
		conn.commit()
	elif opcion=='6':
		idCurso = int(input("Ingresa el id del curso a borrar: "))
		for row in conn.execute('SELECT * FROM curso ORDER BY idCurso ASC'):
			print("id curso: ",row[0]," Nombre curso: ",row[1],"Cupo: ",row[2])
		cursor.execute("DELETE FROM curso WHERE idCurso=%d"%idCurso)
		print("Curso eliminado correctamente!")
		conn.commit()		
	elif opcion=='7':
		for row in conn.execute('SELECT * FROM alumno ORDER BY folio DESC'):
			print("Folio: ",row[0]," Nombre: ",row[1],row[2],row[3])	
		folio = int (input("Ingresa el folio del que deseas actualizar: "))
		opcioncambio = int(input("¿Qué campo quieres cambiar? : \n1.-Folio\n2.-Nombre\n3.-Apellido Paterno\n4.-Apellido Materno"))
		if opcioncambio ==1:
			nuevofolio = int(input("Ingresa el nuevo folio: "))
			cursor.execute("""
				UPDATE alumno SET folio = "%d" WHERE folio=%d
				"""%(nuevofolio,folio))		
			conn.commit()
			print("Usuario actualizado.")
	elif opcion=='8':
		pass
	elif opcion=='9':
		pass
	elif opcion=='10':
		pass
	elif opcion=='11':
		print("Gracias por utiizar la pyDB, hasta pronto!")
		break
	#else:
	#	print("Opción incorrecta, intenta de nuevo!")



#Ver todos los datos de la tabla

#for row in conn.execute('SELECT * FROM alumnos ORDER BY promedio DESC'):
#	print("Nombre: ",row[1],"Promedio: ",row[2])

#Cerrar la conexión
conn.close()