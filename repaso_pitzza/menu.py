class Menu():
    
    id             = int
    nombre         = str
    descripcion    = str
    precio         = int
    disponibilidad = bool
    
    def __init__(self,id,nombre,descripcion,precio,disponibilidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion 
        self.precio = precio
        self.disponibilidad = disponibilidad
        