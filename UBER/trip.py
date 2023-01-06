from car import Car
from acount_driver import Driver
from acoun_User import User
from Route import Route
from payment import Pago

class Trip : 
    
    id_trip = int
    car = Car ("","","","" )
    driver = Driver("","","","","","")
    user = User("","","","","")
    route = Route ("","","","" )
    pago = Pago ("","","" )
    
    def __init__(self ,car , driver , user , route , pago):
        
        self.car = car
        self.driver = driver
        self.user = user
        self.route = route
        self.pago = pago
        

        


