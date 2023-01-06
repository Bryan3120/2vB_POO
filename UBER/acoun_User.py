from acount import Cuenta

class User(Cuenta):
   
    def __init__(self, nombre, apellido, cedula, telefono, ids ):
        super().__init__(nombre, apellido, cedula, telefono, ids)
       