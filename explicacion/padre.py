#HERENCIA EN PYTHON
class Persona:
    nombre   = str
    apellido = str

    def __init__(self, nombre, apellido):
        self.nombre   = nombre
        self.apellido = apellido
        
    def imprimir(self):
        print(self.nombre, self.apellido)

x = Persona("Bryan", "Caicedo")
x.imprimir()

# HERENCIA SIMPLE EN PYTHON
class Studiante(Persona):
    pass

y = Studiante("Luis", "Caizatoa")
y.imprimir()

#Agregar atributos a una herencia
class Student(Persona):
    edad =  int
    
    def __init__(self, nombre, apellido, edad):
        Persona.__init__(self,nombre, apellido)
        self.edad = edad

estudiante1 = Student("Jenifer", "Lopez", 28)
estudiante1.imprimir()

# AGREGAR METODOS A UNA HERENCIA

class Student1(Persona):
    edad     = int
    semestre = str
    
    def __init__(self, nombre, apellido, edad, semestre):
        super().__init__(nombre, apellido)
        self.edad     = edad
        self.semestre = semestre
    
    def bienvenido(self):
        print("Bienvenido " + self.apellido + " al " + self.semestre + " ingresas a los " + str(self.edad) + " años")

p5 = Student1("Bryan", "Caicedo", 20, "Segundo")
p5.bienvenido()