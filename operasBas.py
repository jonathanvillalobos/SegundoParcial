import os

os.system("cls")

'''
Docstring for operasBas

realizae
1.- +
2.- -
3.- *
4.- /
5.- salir

pedir la opcion con menu() y cada operacion sera una funcion,
suma(), resta(), multiplicacion(), division()



'''

'''

MI VERSION (tiene fallas)

print("Operaciones basicas \n1.- suma \n2.- resta \n3.- multiplicacion \n4.- division ")
menu=int(input("Seleccione una opcion (1/2/3/4)\n : "))



while 0 < menu <= 5:
 if menu == 1:
    def suma():
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))
        su = a + b
        return su

    print("La suma es:", suma())  #la sangria es importante
    
 if menu == 2:
    def resta():
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))
        re = a - b
        return re

    print("La resta es:", resta()) 
    
 if menu == 3:
    def multiplicacion():
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))
        mo = a*b
        return mo

    print("La multiplicacion es:", multiplicacion())
    
 if menu == 4:
    def division():
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))
        di = a/b
        return di
    
    print("La division es:", division())
    
 if menu == 5:
    print("Presione enter para continuar...")

    print("La division es:", division())  
print("Opcion invalida.")

'''






#VERSION DE LA IA (para ver mis errores)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0"
    return a / b


menu = 0

while menu != 5:
    print("\n--- MENU ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    menu = int(input("Seleccione una opcion: "))

    if menu >= 1 and menu <= 4:
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))

    if menu == 1:
        print("La suma es:", suma(a, b))

    elif menu == 2:
        print("La resta es:", resta(a, b))

    elif menu == 3:
        print("La multiplicacion es:", multiplicacion(a, b))

    elif menu == 4:
        print("La division es:", division(a, b))

    elif menu == 5:
        print("Saliendo del programa...")

    else:
        print("Opcion invalida.")
        
