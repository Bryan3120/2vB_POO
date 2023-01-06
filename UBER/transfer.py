from payment import Pago
class Transfer(Pago): 
    cuenta =  int
    banco = str
    datost = []
    
    
    def __init__(self, id, fecha, valor , cuenta ,banco ,datost):
        super().__init__(id, fecha, valor)
        self.cuenta  = cuenta
        self.banco = banco
        self.datost = datost
        