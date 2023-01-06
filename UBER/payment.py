

class Pago(): 
    id = str
    fecha = int
    valor = float
    
    def __init__(self, id, fecha, valor):
        self.id = id 
        self.fecha = fecha  
        self.valor = valor