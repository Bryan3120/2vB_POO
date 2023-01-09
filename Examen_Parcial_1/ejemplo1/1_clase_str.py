"""
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def __str__(self):
        cadena=self.nombre+", "+self.apellido
        return cadena

persona1=Persona("Bryan", "Caicedo")
print(persona1)
"""
#ejercicio 1

class Punto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"
    
#bloque principal

punto1 = Punto(23, 12)
punto2 = Punto(3, 10)
print(punto1)
print(punto2)