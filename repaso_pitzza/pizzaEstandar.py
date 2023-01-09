from menu import Menu

class PizzaEstandar(Menu):
    
    ingredientes = [str, str]
    
    def __init__(self, id, nombre, descripcion, precio, disponibilidad, ingredientes):
        super().__init__(id, nombre, descripcion, precio, disponibilidad)
        self.ingredientes = ingredientes