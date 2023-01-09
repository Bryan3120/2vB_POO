from account import Account


class Admin(Account):

    acceso = bool

    def __init__(self, id, nombre, mail, direccion, telefono, acceso):
        super().__init__(id, nombre, mail, direccion, telefono)
        self.acceso = acceso
