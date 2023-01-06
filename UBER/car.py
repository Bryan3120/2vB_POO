from acount_driver import Driver
class Car : 
    placa = str
    año = int
    color = str
    drive = Driver("","","","","","")
   
    def __init__(self , placa , año , color, driver):
        super().__init__ 
        self.placa = placa
        self.año= año
        self.color = color        
        self.drive = driver
        
    