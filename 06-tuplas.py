tupla=(1,2,3,4,5) 
print(type(tupla))
print("el elemento de la tupla es: ", tupla[2]) #dara la posicion "2" o sea el numero "3"

for i in tupla:    #para imprimir valor por valor 
    print (i)  
    
print("La cantidad de elementos de la tupla es : ", len(tupla))

print("la cantidad de veces que se repite el numero 2 es: ", tupla.count(2))

print ("el indice del numero 3 es: ", tupla.index(3))

datos = ("juan", 20 , True)

#Tupla.append (genera un error porque a las tuplas no se le puede agregar algo)


una_tupla = (5)
una_tupla=(5,)
print (datos)
print (una_tupla)