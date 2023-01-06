class Provincia:
    nombre      = str
    habitantes  = int
    capital     = str
    area        = int

    def __init__(self, nombre, habitantes, capital, area):
        self.nombre     = nombre
        self.habitantes = habitantes
        self.capital    = capital
        self.area       = area
