
from car import  Car

class uberfx(Car): 
    aceptado = bool
    asientos = int
    tapisado = str
    
    def __init__(self, placa, ao, color, conductor, driver , asientos , aceptado ,tapisado):
        super().__init__(placa, ao, color, conductor, driver)
        self.asientos = asientos
        self.tapisado = tapisado
        self.aceptado = aceptado
        