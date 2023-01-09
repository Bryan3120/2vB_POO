from catalogo import Catalogo

class Laptop(Catalogo):
    
    marca    = str
    memoria  = [str, str]
    
    def __init__(self,id,nombre,descripcion, precio, disponibilidad, memoria, marca):
        super().__init__(id, nombre, descripcion, precio, disponibilidad)
        self.marca
        self.memoria