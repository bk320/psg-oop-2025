class Martillo:
    def __init__(self, tipo_mango, material, peso):
        self.tipo_mango = tipo_mango
        self.material = material
        self.peso = peso
    
    def usar(self):
        print("Golpeando con el martillo.")

class Destornillador:
    def __init__(self, tipo_mango, material, peso):
        self.tipo_mango = tipo_mango
        self.material = material
        self.peso = peso
    
    def usar(self):
        print("Atornillando con el destornillador.")

class Llave_inglesa:
    def __init__(self, tipo_mango, material, peso):
        self.tipo_mango = tipo_mango
        self.material = material
        self.peso = peso
    
    def usar(self):
        print("Ajustando con la llave inglesa.")
        
class Carpintero:
    def usar_herramienta(self, objeto):
        objeto.usar()
        
# Ejemplo de uso
carpintero = Carpintero()
martillo = Martillo("madera", "acero", 1.5)
destornillador = Destornillador("plástico", "acero", 0.5)
llave_inglesa = Llave_inglesa("goma", "acero", 2.0)

carpintero.usar_herramienta(martillo)
carpintero.usar_herramienta(destornillador)
carpintero.usar_herramienta(llave_inglesa)