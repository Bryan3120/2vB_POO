from account import Account

class User(Account):
    
    def __init__(self,id,nombre, mail,direccion,telefono):
        super().__init__(id,nombre,mail,direccion,telefono)
        
    def __str__(self):
        return f'El nombre del cliente es: {self.nombre}'
    
    