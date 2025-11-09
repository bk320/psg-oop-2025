class Instrumento:
    def __init__(self, marca, modelo, material):
        self.marca = marca
        self.modelo = modelo
        self.material = material

class Guitarra(Instrumento):
    def __init__(self, marca, modelo, material, num_cuerdas):
        super().__init__(marca, modelo, material)
        self.num_cuerdas = num_cuerdas
    def tocar(self):
        print("strum")

class Piano(Instrumento):
    def __init__(self, marca, modelo, material, num_teclas):
        super().__init__(marca, modelo, material)
        self.num_teclas = num_teclas
    def tocar(self):
        print("plin")

class Bateria(Instrumento):
    def __init__(self, marca, modelo, material, tipo_percusion, diametro):
        super().__init__(marca, modelo, material)
        self.tipo_percusion = tipo_percusion
        self.diametro = diametro
    def tocar(self):
        print("boom")

class Usuario:
    def tocar_instrumento(self, instrumento):
        instrumento.tocar()

# Ejemplo de uso
usuario = Usuario()
guitarra = Guitarra("Fender", "Stratocaster", "Madera", 6)
piano = Piano("Yamaha", "U3", "Madera", 88)
bateria = Bateria("Pearl", "Export", "Metal", "Acústica", 21.5)

usuario.tocar_instrumento(guitarra)
usuario.tocar_instrumento(piano)
usuario.tocar_instrumento(bateria)
