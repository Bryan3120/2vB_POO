from compra import CompraCelular
from compra import CompraLaptop
from compra import CompraPC

class Pago1(CompraCelular):
    id          = int
    metodoPago  = str
    fecha       = int
    pedido      = CompraCelular("", "", "", "", "", "")
    
    def __init__(self, id, metodoPago, fecha, pedido):
        self.id         = id
        self.metodoPago = metodoPago
        self.fecha      = fecha
        self.pedido     = pedido
    
    def __str__(self):
        return f'Hola {self.pedido.cliente.nombre}, El monto a pagar es: ${self.pedido.celularGaming.precio}. Quien le atendio fue: {self.pedido.vendedor.nombre}. REGRESA PRONTO GUSTO ATENDERTE!!'
    
class Pago2(CompraLaptop):
    id          = int
    metodoPago  = str
    fecha       = int
    pedido      = CompraLaptop("", "", "", "", "", "")
    
    def __init__(self, id, metodoPago, fecha, pedido):
        self.id         = id
        self.metodoPago = metodoPago
        self.fecha      = fecha
        self.pedido     = pedido
    
    def __str__(self):
        return f'Hola {self.pedido.cliente.nombre}, El monto a pagar es: ${self.pedido.laptop.precio}. Quien le atendio fue: {self.pedido.vendedor.nombre}. REGRESA PRONTO GUSTO ATENDERTE!!'
    
class Pago3(CompraPC):
    id          = int
    metodoPago  = str
    fecha       = int
    pedido      = CompraPC("", "", "", "", "", "")
    
    def __init__(self, id, metodoPago, fecha, pedido):
        self.id         = id
        self.metodoPago = metodoPago
        self.fecha      = fecha
        self.pedido     = pedido
    
    def __str__(self):
        return f'Hola {self.pedido.cliente.nombre}, El monto a pagar es: ${self.pedido.pc.precio}. Quien le atendio fue: {self.pedido.vendedor.nombre}. REGRESA PRONTO GUSTO ATENDERTE!!'