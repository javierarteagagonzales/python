#TEMA:IF

###########################################################################

def evaluacion(nota):
	valoracion = "Aprobado"
	if nota<5:
		valoracion="Suspenso"
	return valoracion


###########################################################################	
#Llamada de la funcion
print("Ejemplo #1")
print(evaluacion(4))
print()
print()
print()

###########################################################################
#Tomar valor del teclado
print("Ejemplo #2")
print("Introduce la nota del alumno: ")
notaAlumno=input() #Coge el valor por consola
#notaAlumno = int(notaAlumno) #Convierte el valor a entero
print(evaluacion(int(notaAlumno)))
print()
print()
print()

##########################################
##Importantes el Ambito de las Variables##
##########################################


