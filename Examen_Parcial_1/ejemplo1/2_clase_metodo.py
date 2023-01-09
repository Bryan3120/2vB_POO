class Alumno:
    def __init__(self, nombre, apellido, edad, nota):
        self.name     = nombre
        self.apellido = apellido
        self.edad     = edad
        self.nota     = nota
    
    def imprimir(self):
        print("Nombre: ", self.name)
        print("Apellido: ", self.apellido)
        print("Edad: ", self.edad)
        print("Nota: ", self.nota)
        
    def mostrar_estado(self):
        if self.nota >= 4:
            print("Regular")
            
        else:
            print("Libre")
            
#bloque principal

alumno1=Alumno("Bryan", "Caicedo", 20, 8)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno("Luis", "Caizatoa", 30, 2)
alumno2.imprimir()
alumno2.mostrar_estado()
    