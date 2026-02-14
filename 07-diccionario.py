import os
os.system("cls")



''' Un diccionario es una estrcutrua de datos
que alamacena informacion en pares clave-valor


no se accede por posicion si no por clave

ejemplo:
alumno = {
    "nombre": "ana",
    "edad": 21,
    "carrera": "ingenieria"
}
'''




alumno = {
    "Nombre": "Ana",
    "Edad": 21,
    "Carrera": "Ingenieria"
}
print(type(alumno))
print(alumno)

print(alumno['Nombre'])  #para imprimir los datos

#agregar o modificar datos 

alumno["Edad"] = 22

alumno["promedio"] = 9.2

#Eliminar valor-valor

del alumno["Carrera"]
print(alumno)

#para recorrer un diccionario

for clave in  alumno:
    print(clave)
    print(clave,":", alumno[clave])
    


#funciones utiles para el diccionario

print("cantidad parees clave-valor. ", len(alumno))
print("claves diccionario: ",alumno.keys())
print("Valores del diccionario: ",alumno.values())
print("pares clave-valor: ",alumno.items())


#para tener mas alumnos 

ICO201=[alumno1,alumno1,alumno1]