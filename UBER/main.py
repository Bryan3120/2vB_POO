from acount import Cuenta
from acount_driver import Driver
from acoun_User import User
from car import Car
from payment import Pago
from transfer import Transfer
from Route import Route
from trip import Trip
from uberfx import uberfx
from ubercomfort import  ubercomfort
from uberX import uberx 


if __name__ == "__main__" : 
    usuario1 = User("Bryan", "Caicedo", 1712324323, 123123123, 12 )
    usuario2 = User("Josue", "Rodriguez", 1212123123 , 12312312312 , 11)
    carro1 = Car("PPB-679", "2016", "Café" ,  Driver("Alex", "Perez", 1734543423, 12312312312, 1, "Licencia"))
    ruta1 = Route([-21321321321, -12341654654], [564654 , -4654654], "5.1km" , "22min")
    pago1 = Pago (1, 10-12-2022, "10$")
    conductor = Driver("Raul", "Loor", 172321232123, 12312312312, 11, "Licencia")  
    
    """
    print (vars(carro_1))
    print (vars(carro_1.drive)) 
    pagooo1 = Transfer ( 1,1,"115-10-2022", 5555 , "pichincha" , [4546545 , 20,"josue" , 54584])
    print(vars(pago1))   
    print( vars(pago2))   
    print( vars(ruta_uno))
    """

     
     
    trip002 = Trip(Car("pbc-123", "2020","red" ,  Driver("Bryan", "Caicedo", 17233123123, 1233123123, 12, "Licencia")),
                   Driver("Raul", "Loor", 172321232123, 1233123123, 12, "Licencia"),
                   User("Josue", "Rodriguez", 172321232, 1233123123, 23),
                   Route([-21321321321, -12341654654],[564654 , -4654654] , "4.3km" , "19min"),
                   Pago(2, 10-12-2022, "10$"))
   
    print(vars(trip002))
    print(vars(trip002.driver))
    print(vars(trip002.car))
    print(vars(trip002.user))
    print(vars(trip002.route))
    print(vars(trip002.pago))
    
    
    trip001 = Trip(carro1, conductor, usuario1 , ruta1 , pago1 )
    print(vars(trip001.car.drive))
    print(vars(trip001.car))
    print(vars(trip001.user))
    print(vars(trip001.route))
    print(vars(trip001.pago))
    
    
  
    
    
    
    
    