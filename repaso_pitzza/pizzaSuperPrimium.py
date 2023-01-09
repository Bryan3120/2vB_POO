from menu import Menu

class PizzaSuperPrimium(Menu):
    
    ingredientes    = [str, str, str, str, str, str]
    
    def __init__(self,id,nombre,descripcion, precio, disponibilidad, ingredientes):
        super().__init__(id,nombre,descripcion, precio, disponibilidad)
        self.ingredientes