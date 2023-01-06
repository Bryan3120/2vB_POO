from acount import Cuenta

class Driver(Cuenta):
    licensia = int
    def __init__(self, nombre, apellido, cedula, telefono, ids , licensia):
        super().__init__(nombre, apellido, cedula, telefono, ids)
        self.licensia = licensia
    