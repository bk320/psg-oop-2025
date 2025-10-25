class Vehiculo:
    def __init__(self, velocidad, medio):
        self._velocidad = velocidad
        self.medio = medio
    def mostrar(self):
        print(f"Velocidad: {self._velocidad} km/h, Medio: {self.medio}")

class Bicicleta(Vehiculo):
    def __init__(self, velocidad, medio):
        super().__init__(velocidad, medio)
    def pedalear(self):
        self._velocidad += 10
        print(f"La bicicleta a incrementado su velocidad a {self._velocidad} km/h")
    def mostrar(self):
        print("Bicicleta")
        super().mostrar()

class Avion(Vehiculo):
    def __init__(self, velocidad, medio):
        super().__init__(velocidad, medio)
    def volar(self):
        self._velocidad += 820
        print(f"El avion a incrementado su velocidad a {self._velocidad} km/h")
    def mostrar(self):
        print("Avion")
        super().mostrar()
        
# Ejemplo de uso, incremente el motodo mostrar para poder utilizar en los ejemplos
bicicleta = Bicicleta(3, "terrestre")
bicicleta.mostrar()
bicicleta.pedalear()
avion = Avion(222, "aéreo")
avion.mostrar()
avion.volar()