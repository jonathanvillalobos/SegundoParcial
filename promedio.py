# Lista donde se guardarán todos los alumnos
alumnos = []

# Pedir cantidad de alumnos
cantidad = int(input("¿Cuántos alumnos deseas ingresar? "))

# Ciclo para ingresar los datos
for i in range(cantidad):
    print("\nAlumno " + str(i + 1)) #sin el str me da error porque texto y numeros no se unen
    edad = input("Ingresa la edad: ")
    nombre = input("Ingresa el nombre: ")
    materia = input("Ingresa la materia: ")
    calificacion = int(input("Ingresa la calificacion: "))
    
    # Crear diccionario para cada alumno
    alumno = {
        "nombre": nombre,
        "edad": edad,
        "materia": materia,
        "calificacion": calificacion    
    }
    
    # Agregar diccionario a la lista
    alumnos.append(alumno)

# Mostrar los datos guardados
print("\n--- Lista de Alumnos ---")
for i in range(len(alumnos)):   #len es la longitud de la lista (para saber cuantos alumnos hay)
    print("\nAlumno " + str(i + 1))
    print("Nombre: " + alumnos[i]["nombre"])
    print("Edad: "+ alumnos[i]["edad"])
    print("Materia: " + alumnos[i]["materia"])
 
 

suma=0    
for i in range(len(alumnos)):
    suma = alumnos[i]["calificacion"] + suma #Para poder sumar cualquier cossa ocupamos esta suma

promedio=suma/len(alumnos)
   
print("El promedio es: ",promedio)