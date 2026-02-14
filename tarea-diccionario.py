# Lista donde se guardarán todos los alumnos
alumnos = []

# Pedir cantidad de alumnos
cantidad = int(input("¿Cuántos alumnos deseas ingresar? "))

# Ciclo para ingresar los datos
for i in range(cantidad):
    print("\nAlumno " + str(i + 1))
    edad= int(input("Ingresa la edad: "))
    nombre = input("Ingresa el nombre: ")
    carrera = input("Ingresa la carrera: ")
    
    # Crear diccionario para cada alumno
    alumno = {
        "nombre": nombre,
        "carrera": carrera,
        "edad": edad
    }
    
    # Agregar diccionario a la lista
    alumnos.append(alumno)

# Mostrar los datos guardados
print("\n--- Lista de Alumnos ---")
for i in range(len(alumnos)):
    print("\nAlumno " + str(i + 1))
    print("Nombre: " + alumnos[i]["nombre"])
    print("edad: "+ edad[i]["edad"])
    print("Carrera: " + alumnos[i]["carrera"])
    