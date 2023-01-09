from accountAdmin import Admin
from accountDelivery import Delivery
from accountUser import User
from pizzaEstandar import PizzaEstandar
from pizzaPrimium import PizzaPrimium
from pizzaSuperPrimium import PizzaSuperPrimium

# PizzEstandar


class PedidoPizzaEstandar(Admin, Delivery, User, PizzaSuperPrimium, PizzaEstandar, PizzaPrimium):
    id                  = int
    vendedor            = Admin("", "", "", "", "", "")
    cliente             = User("", "", "", "", "")
    delivery            = bool
    pizzaEstandar       = PizzaEstandar("", "", "", "", "", "")
    horaPedido          = int
    horaEntrega         = int
    
    def __init__(self, id, vendedor, cliente, delivery, pizzaEstandar, horaPedido, horaEntrega):
        self.id             = id
        self.vendedor       = vendedor
        self.cliente        = cliente
        self.delivery       = delivery
        self.pizzaEstandar  = pizzaEstandar
        self.horaEntrega    = horaEntrega
        self.horaPedido     = horaPedido

# PizzaPrimium


class PedidoPizzaPrimium(Admin, Delivery, User, PizzaEstandar, PizzaPrimium, PizzaSuperPrimium):
    id           = int
    vendedor     = Admin("", "", "", "", "", "")
    cliente      = User("", "", "", "", "")
    delivery     = bool
    pizzaPrimium = PizzaPrimium("", "", "", "", "", "")
    horaPedido   = int
    horaEntrega  = int


def __init__(self, id, vendedor, cliente, delivery, pizzaPrimium, horaPedido, horaEntrega):
    self.id           = id
    self.vendedor     = vendedor
    self.cliente      = cliente
    self.delivery     = delivery
    self.pizzaPrimium = pizzaPrimium
    self.horaPedido   = horaPedido
    self.horaEntrega  = horaEntrega

# PizzaSuperPrimium


class PedidoPizzaSuperPrimium(Admin, Delivery, User, PizzaEstandar, PizzaPrimium, PizzaSuperPrimium):
    id                = int
    vendedor          = Admin("", "", "", "", "", "")
    cliente           = User("", "", "", "", "")
    delivery          = bool
    pizzaSuperPrimium = PizzaSuperPrimium("", "", "", "", "", "")
    horaPedido        = int
    horaEntrega       = int


def __init__(self, id, vendedor, cliente, delivery, pizzaSuperPrimium, horaPedido, horaEntrega):
    self.id                = id
    self.vendedor          = vendedor
    self.cliente           = cliente
    self.delivery          = delivery
    self.pizzaSuperPrimium = pizzaSuperPrimium
    self.horaPedido        = horaPedido
    self.horaEntrega       = horaEntrega
