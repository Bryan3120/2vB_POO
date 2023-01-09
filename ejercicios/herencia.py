class Persona:
    
    def __init__(self):
        self.nombre   = input('Ingrese su nombre:')
        self.apellido = input('Ingrese su apellido:')
        
    def imprimir(self):
        print('Nombre: ' + self.nombre)
        print('Apellido:'+ self.apellido)
        
class Empleado(Persona):
    
    def __init__(self):
        super().__init__()
        self.sueldo=float(input('Ingrese el sueldo:'))
        
    def imprimir(self):
        super().imprimir()
        print('Sueldo', self.sueldo)
        
    def paga_impuesto(self):
        if self.sueldo>3000:
            print('El empeado debe pagar impuesto')
        else:
            print('No paga impuesto')
            
# Bloque

persona1 = Persona()
persona1.imprimir()
print("_____________________")
empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuesto()