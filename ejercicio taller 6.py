class Paciente:
    def __init__(self, identificacion, nombres, estrato):
        self.identificacion = identificacion
        self.nombres = nombres
        self.estrato = estrato

    def guardar(self):
        archivo = open("Paciente.txt", "a")
        archivo.write(self.identificacion + "," + self.nombres + "," + str(self.estrato) + "\n")
        archivo.close()

p1 = Paciente("123456", "Carlos Perez", 2)
p1.guardar()