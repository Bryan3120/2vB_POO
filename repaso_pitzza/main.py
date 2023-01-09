from account import Account
from accountAdmin import Admin
from accountDelivery import Delivery
from accountUser import User
from pedido import PedidoPizzaEstandar
from pizzaEstandar import PizzaEstandar
from pago import Pago

if __name__ == "__main__":
    
    alex   = Admin(1, "Alex Marcos", "alex@gmail.com", [5555333, 55556668], 989767876, True)
    print(vars(alex))
    
    victor = User(2, "Victor Fuentes", "victor@gmail.com", [555, 666], 4243454)
    marco  = User(3, "Marco Alonso", "marco@gmail.com", [555, 666], 4532332)
    print(vars(victor))
    
    jorge  = Delivery(1, "Jorge Lopez", 987564567, "Licencia", "PPB-456", "Motocicleta Suziki")
    print(vars(jorge))
    
    pizzaEstandar1 = PizzaEstandar(1, "Pizza Estandar", "Pizza dos ingredientes", 20, True, ["Peperoni", "Salami"])
    
    pedido1 = PedidoPizzaEstandar(1, Admin(1, "Alex Marcos", "alex@gmail.com", [5555333, 55556668], 989767876, True), 
                                  User(2, "Victor Fuentes", "victor@gmail.com", [555, 666], 4243454), False, 
                                  PizzaEstandar(1, "Pizza Estandar", "Pizza dos ingredientes", 20, True, ["Peperoni", "Salami"]),
                                  1800, 1830)
    print(vars(pedido1))
    print(pedido1.cliente)
    
    pedido2 = PedidoPizzaEstandar(2, "Alex", "Victor", "Jorge", pizzaEstandar1, 1800, 1830)
    print(vars(pedido2))
    print(pedido2.cliente)
    
    pago1 = Pago(1, "Efectivo", 8-1-2023, PedidoPizzaEstandar(1, 
                Admin(1, "Alex Marcos", "alex@gmail.com", [5555333, 55556668], 989767876, True), 
                User(3, "Marco Alonso", "marco@gmail.com", [555, 666], 4532332), False, 
                PizzaEstandar(1, "Pizza Estandar", "Pizza dos ingredientes", 20, True, ["Peperoni", "Salami"]), 
                1700, 1730))
    print(vars(pago1))
    print(vars(pago1.pedido))
    print(vars(pago1.pedido.cliente))
    
    pago2 = Pago(2, "efectivo", 12012023, pedido2)
    print(vars(pago2))