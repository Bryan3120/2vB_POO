from accountAdmin import Admin
from accountEntrega import Entrega
from accountUser import User
from celular import CelularGaming
from laptop import Laptop
from pc import PC

# Celulares


class CompraCelular(Admin, Entrega, User, CelularGaming, Laptop, PC):
    id                  = int
    vendedor            = Admin("", "", "", "", "", "")
    cliente             = User("", "", "", "", "")
    entrega             = bool
    celularGaming       = CelularGaming("", "", "", "", "", "", "")
    horaCompra          = int
    
    def __init__(self, id, vendedor, cliente, entrega, celularGaming, horaCompra):
        self.id             = id
        self.vendedor       = vendedor
        self.cliente        = cliente
        self.entrega        = entrega
        self.celularGaming  = celularGaming
        self.horaCompra     = horaCompra    

# Laptops


class CompraLaptop(Admin, Entrega, User, CelularGaming, Laptop, PC):
    id                  = int
    vendedor            = Admin("", "", "", "", "", "")
    cliente             = User("", "", "", "", "")
    entrega             = bool
    laptop              = Laptop("", "", "", "", "", "", "")
    horaCompra          = int
    
    def __init__(self, id, vendedor, cliente, entrega, laptop, horaCompra):
        self.id             = id
        self.vendedor       = vendedor
        self.cliente        = cliente
        self.entrega        = entrega
        self.laptop         = laptop    
        self.horaCompra     = horaCompra    

# PC


class CompraPC(Admin, Entrega, User, CelularGaming, Laptop, PC):
    id                  = int
    vendedor            = Admin("", "", "", "", "", "")
    cliente             = User("", "", "", "", "")
    entrega             = bool
    pc                  = PC("", "", "", "", "", "", "")
    horaCompra          = int
    
    def __init__(self, id, vendedor, cliente, entrega, pc, horaCompra):
        self.id             = id
        self.vendedor       = vendedor
        self.cliente        = cliente
        self.entrega        = entrega
        self.pc             = pc  
        self.horaCompra     = horaCompra    
