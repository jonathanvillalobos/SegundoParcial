class persona :
    def inicializar(self,nom): #En las clases se poone self (solo en clases)
        self.nombre=nom
    def imprimir(self):
        print("Nombre",self.nombre)
        
persona1=persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2=persona()
persona2.inicializar("Carla")
persona2.imprimir()

class operasbas:
    n1=0
    n2=0
    res=0
    def sumar(self):
        self.res = self.n1 + self.n2
        return self.res
    
    def resta(self):
        self.res = self.n1 - self.n2
        return self.res
    
    def division(self):
        self.res = self.n1 / self.n2
        return self.res
    
    def multiplicar(self):
        self.res = self.n1 *self.n2
        return self.res
    
    def pedirnumero(self):
        self.n1=int(input("n1: "))
        self.n2=int(input("n2: "))
       # print("ls suma es: ",self.sumar(self.n1,self.n2))
        
obj=operasbas()
obj.pedirnumero()

print("La suma es: ",obj.sumar())


def main():
    obj=operasbas
    obj.pedirnumero
    print("La suma es : ", obj.sumar())
    
if __name__=="__main__":
    main()