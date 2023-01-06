class persona:
    nombre = str
    edad   = int
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad   = edad
        
    def saluda (self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.' 
    
if __name__ == "__main__":
    Persona1 = persona("Bryan", 33)
    Persona2 = persona("Luis", 35)
    
    print (Persona1.saluda(Persona2))
    
class MiClase:
    nombre  = "Bryan"
    edad    = 20

p1 = MiClase()
print(p1.nombre)

# la funcion __init__()

class persona2:
    nombre = str
    edad   = int
    genero = str
    
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad   = edad
        self.genero = genero

p2 = persona2("Bryan", 29, "Masculino")

print(p2.nombre)
print(p2.edad)
print(p2.genero)

#La funcion __str__()

class persona3:
    nombre   = str
    edad     = int
    genero   = str
    estatura = int
    
    def __init__(self, nombre, edad, genero, estarura):
        self.nombre   = nombre
        self.edad     = edad
        self.genero   = genero
        self.estatura = estarura

    def __str__(self):
        return f'Hola me llamo {self.nombre}, tengo {self.edad} años, estatura: {self.estatura} cm; Genero: {self.genero}'

p3 = persona3("Bryan", 20, "Masculino", 171)

print(p3)

# Metodos dentro de Objetos

class persona4:
    nombre   = str
    semestre = str

    def __init__(self, nombre, semestre):
        self.nombre   = nombre
        self.semestre = semestre

    def saludo(self):
        print("Bienvenido " + self.nombre + " al " + self.semestre + " semestre")

p4 = persona4("Bryan", "Segundo")
p4.saludo()

p4.nombre = "Luis"
p4.saludo()

#del p4.semestre
#p4.saludo()




