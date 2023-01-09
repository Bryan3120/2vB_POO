class Padre:
    nombre   = str
    apellido = str
    edad     = int

    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad

        

class Hijo1(Padre):
    ciudad   = str
    
    def __str__(self):
        return f'hola {self.nombre} {self.apellido}, tiene {self.edad} años y vive en la ciudad de {self.ciudad}'

if __name__ == '__main__':
    persona1 = Hijo1('Bryan', 'Caicedo', 20)
    print(vars(persona1))