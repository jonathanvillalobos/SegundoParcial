import os, math

os. system("cls")

def menu ():
    print("\n--- MENU ---")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Triangulo")
    print("4. Circulo")
    print("5. Trapecio")
    print("6. Salir")
    
    
def Cuadrado(a):
    return a * 2
    input()

def Rectangulo(a, b):
    return a * b
    input()
def Triangulo(a, b):
    return (a * b)/2
    input()

def Circulo(a):
    return a* (3.1416**2)
    input()
def Trapecio(a,b,c):
    return ((a+b)*c)/2
    input()
    
m=0

while m != 6:
    
    menu()

    m= int(input("Seleccione una opcion: "))
    

    if m == 1:
        a = int(input("Ingrese el lado: "))
        print("El area del cuadrado es: ", Cuadrado(a))
        input("Presiona para continuar bro...")

    elif m == 2:
        a = int(input("Ingrese la base: "))
        b = int(input("Ingrese La altura: "))
        print("El area del rectangulo e: ", Rectangulo(a, b))
        input("Presiona para continuar bro...")

    elif m == 3:
        a = int(input("Ingrese la base: "))
        b = int(input("Ingrese La altura: "))
        print("El area del triangulo es:", Triangulo(a, b))
        input("Presiona para continuar bro...")

    elif m == 4:
        a = int(input("Ingrese el radio: "))
        print("La division es:", Circulo(a, b))
        input("Presiona para continuar bro...")

    elif m == 5:
        a = int(input("Ingrese la base mayor: "))
        b = int(input("Ingrese La base menor: "))
        c = int(input("Ingrese la altura: "))
        print("El area del trapecio es: ", Trapecio(a,b,c))
        input("Presiona para continuar bro...")

    else:
        print("Opcion invalida.")
        input("Presiona para continuar bro...")
        
