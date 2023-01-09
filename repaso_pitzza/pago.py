from pedido import PedidoPizzaEstandar

class Pago(PedidoPizzaEstandar):
    id          = int
    metodoPago  = str
    fecha       = int
    pedido      = PedidoPizzaEstandar("", "", "", "", "", "", "")
    
    def __init__(self, id, metodoPago, fecha, pedido):
        self.id         = id
        self.metodoPago = metodoPago
        self.fecha      = fecha
        self.pedido     = pedido
    
    def __str__(self):
        return f'Hola {self.pedido.cliente.nombre}, El monto a pagar es: ${self.pedido.pizzaEstandar.precio}. Quien le atendio fue: {self.pedido.vendedor.nombre}. REGRESA PRONTO TE EXTRAÑAREMOS!!'