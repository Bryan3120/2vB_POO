from archivo1 import Pais
from archivo2 import Provincia

# Herencia simple dentro del mismo archivo


class Padre1:
    nombre = str
    apellido = str
    edad = int

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


class Hijo1(Padre1):
    ciudad = str

    def __init__(self, nombre, apellido, edad, ciudad):
        super().__init__(nombre, apellido, edad)
        self.ciudad = ciudad

# Herencia simple con metodos


class Padre2:
    nombre = str
    apellido = str
    edad = int

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f'Hola {self.nombre} {self.apellido}, tu edad es {self.edad}'


class Hijo2(Padre2):
    ciudad = str

    def __init__(self, nombre, apellido, edad, ciudad):
        super().__init__(nombre, apellido, edad)
        self.ciudad = ciudad


# Herencia de clases con objetos
class Continente(Pais):
    nombre = str
    habitantesContinente = int
    areaContinente = int
    pais = Pais("", "", "", "")

    def __init__(self, nombre, habitantesContinente, areaContinente, pais):
        self.nombre = nombre
        self.habitantesContinente = habitantesContinente
        self.areaContinente = areaContinente
        self.pais = pais


if __name__ == "__main__":

    objeto1 = Hijo1("Bryan", "Caicedo", 20, "Quito")
    print(vars(objeto1))

    objeto2 = Hijo2("Bryan", "Caicedo", 20, "Quito")
    print(objeto2)

    objeto3 = Continente("America", 300000000, 2000000000000, Pais(
        "Ecuador", "Quito", 1854000000, Provincia("Pinchincha", 125000000, "Quito", 420000000)))
    print(vars(objeto3))
    print(vars(objeto3.pais))
    print(vars(objeto3.pais.provincia))
