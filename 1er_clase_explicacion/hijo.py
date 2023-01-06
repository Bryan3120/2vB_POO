from padre import Persona

class Docente(Persona):
    titulo                 = str
    edad                   = int
    experienciaProfesional = int
    experienciaDocente     = int
    
    def __init__(self, nombre, apellido, titulo, edad, experienciaProfesional, experienciaDocente):
        super().__init__(nombre, apellido)
        self.titulo                 = titulo
        self.edad                   = edad
        self.experienciaDocente     =  experienciaDocente
        self.experienciaProfesional = experienciaProfesional

    def BienvenidaDocente(self):
        print("Estimado Docente: " + self.nombre, self.apellido + ". Le damos la bienvenda al IST YAVIRAC " +
              "agradecemos contar con sus " + str(self.experienciaDocente + self.experienciaProfesional) + " años de experiencia")

docente1 = Docente("Diego", "Yanez", "Desarrolador de Software", 24, 2, 1)
docente1.BienvenidaDocente()