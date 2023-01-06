from archivo2 import Provincia

class Pais(Provincia):
    nombre     = str
    capital    = str
    habitantes = int
    provincia  = Provincia("", "", "", "")

    def __init__(self, nombre, capital, habitantes, provincia):
        self.nombre     = nombre
        self.capital    = capital
        self.habitantes = habitantes
        self.provincia  = provincia
