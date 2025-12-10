class Vehiculo:
    def __init__(self, velocidad, medio):
        self._velocidad = velocidad
        self.medio = medio

    @property
    def velocidad(self):
        return self._velocidad

class Bicicleta(Vehiculo):
    def __init__(self, velocidad, medio):
        super().__init__(velocidad, medio)
        
    def pedalear(self):
        self._velocidad += 10
        print(f"La bicicleta a incrementado su velocidad a {self._velocidad} km/h")


class Avion(Vehiculo):
    def __init__(self, velocidad, medio):
        super().__init__(velocidad, medio)
        
    def volar(self):
        self._velocidad += 820
        print(f"El avion a incrementado su velocidad a {self._velocidad} km/h")


bicicleta = Bicicleta(0.2, "terrestre")
print(f"La velocidad inicial de la bicicleta es {bicicleta.velocidad} km/h")
bicicleta.pedalear()

avion = Avion(222, "aéreo")
print(f"\nLa velocidad inicial del avion es {avion.velocidad} km/h")
avion.volar()