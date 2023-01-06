from car import  Car
class ubercomfort(Car): 
    asientos = int
    
    def __init__(self, placa, ao, color, asientos ,driver):
        super().__init__(placa, ao, color, driver)
        self.asientos = asientos
        
