from auto import Auto
from marca import Marca

# HERENCIA SIMPLE DENTRO DEL MISMO ARCHIVO
class Cliente1:
    nombre   = str
    apellido = str
    edad     = int

    def __init__(self, nombre, apellido, edad):
       self.nombre   = nombre
       self.apellido = apellido
       self.edad     = edad
    
class Hijo1(Cliente1):
    ciudad = str

    def __init__(self, nombre, apellido, edad, ciudad):
        super().__init__(nombre, apellido, edad)
        self.ciudad = ciudad

#HERENCIA SIMPLE CON METODOS
class Cliente2:
    nombre = str
    apellido = str
    edad = int

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return f'Hola {self.nombre} {self.apellido}, su edad es {self.edad}'

class Hijo2(Cliente2):
    ciudad = str

    def __init__(self, nombre, apellido, edad, ciudad):
        super().__init__(nombre, apellido, edad)
        self.ciudad = ciudad

#HERENCIA DE CLASES CON OBJETOS
class Cliente3(Marca):
    nombre   = str
    apellido = str
    edad     = int
    ciudad   = str
    marca    = Marca("", "", "")

    def __init__(self, nombre, apellido, edad, ciudad, marca):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        self.ciudad   = ciudad
        self.marca    = marca
    
if __name__ == "__main__":
    
    compra1 = Hijo1('Bryan', 'Caicedo', 20, 'Quito')
    print(vars(compra1))
    
    compra2 = Hijo2('Juan', 'Mata', 20, 'Quito')
    print(vars(compra2))
    
    compra3 = Cliente3('Bryan', 'Caicedo', 20, 'Quito', Marca(
        'Chevrolet', 'Ecuador', Auto('Corsa', 'Gris', 2022)))
    print(vars(compra3))
    print(vars(compra3.marca))
    print(vars(compra3.marca.auto))