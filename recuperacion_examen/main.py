from accountAdmin import Admin
from accountEntrega import Entrega
from accountUser import User
from celular import CelularGaming
from laptop import Laptop
from pc import PC
from compra import CompraCelular
from compra import CompraLaptop
from compra import CompraPC
from pago import Pago1
from pago import Pago2
from pago import Pago3

if __name__ == '__main__':
    jorge   = Admin(1, "Jorge Marcos", "jorge@gmail.com", [5555333, 55556668], 989767876, True)
    print(vars(jorge))
    
    marco = User(2, "Marco Fuentes", "marco@gmail.com", [555, 666], 4243454)
    victor  = User(3, "Victor Alonso", "victor@gmail.com", [555, 666], 4532332)
    print(vars(victor))
    
    alex  = Entrega(1, "Alex Lopez", 987564567, "Licencia", "PPB-456", "Motocicleta Suziki")
    print(vars(alex))
    
    celularGaming = CelularGaming(1, "Black Shark", "Dispositivo movil Gaming", 1000, True, ["250 gb", "ram 12 gb"], "Black Shark")
    
    pc = PC(1, "Asus", "PC Asus Gaming", 1600, True, ["2 Tb", "ram 12 gb"], "Asus")
    
    pedido1 = CompraLaptop(1, Admin(1, "Jorge Marcos", "jorge@gmail.com", [5555333, 55556668], 989767876, True), 
                           User(3, "Victor Alonso", "victor@gmail.com", [555, 666], 4532332), 
                           Entrega(1, "Alex Lopez", 987564567, "Licencia", "PPB-456", "Motocicleta Suziki"), 
                           Laptop(1,"Lenovo", "Laptop Lenovo Gaming", 1200, True, ["2 TB", "ram 16 gb"], "Lenovo"), 1400)
    print(vars(pedido1))
    print(pedido1.cliente)
    
    pedido2 = CompraPC(2, "Jorge", "Marcos", "Alex", pc, 1500)
    
    pago1 = Pago1(1, "Pago en efectivo", 912023, CompraCelular(1, 
                           Admin(1, "Jorge Marcos", "jorge@gmail.com", [5555333, 55556668], 989767876, True), 
                           User(3, "Victor Alonso", "victor@gmail.com", [555, 666], 4532332), False, 
                           CelularGaming(1, "Black Shark", "Dispositivo movil Gaming", 1000, True, ["250 gb", "ram 12 gb"], "Black Shark"),
                           1830))
    print(vars(pago1))
    print(pago1.pedido)
    print(pago1.pedido.cliente)
    
    pago2 = Pago2(1, "Pago en efectivo", 912023, CompraLaptop(1, Admin(1, "Jorge Marcos", "jorge@gmail.com", [5555333, 55556668], 989767876, True), 
                           User(3, "Victor Alonso", "victor@gmail.com", [555, 666], 4532332), False, 
                           Laptop(1,"Lenovo", "Laptop Lenovo Gaming", 1200, True, ["2 TB", "ram 16 gb"], "Lenovo"), 1400))
    print(vars(pago2))
    print(pago2.pedido)
    print(pago2.pedido.cliente)
    
    pago3 = Pago3(1, "Pago en efectivo", 912023, pedido2)
    print(vars(pago3))