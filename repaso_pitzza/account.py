class Account:
    
    id        = int
    nombre    = str
    mail      = str
    direccion = [int,str]
    telefono  = int
    
    def __init__(self, id, nombre, mail, direccion, telefono):
        self.id        = id
        self.nombre    = nombre
        self.mail      = mail
        self.direccion = direccion
        self.telefono  = telefono