from acount import Cuenta

class usuario (Cuenta): 
    def __init__(self, nombre, apellido, cedula, telefono, ids):
        super().__init__(nombre, apellido, cedula, telefono, ids)