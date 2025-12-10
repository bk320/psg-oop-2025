class Minibus:
    def __init__(self, numero_ruta, recorrido, pasajeros):
        self.numero_ruta = numero_ruta
        self.recorrido = recorrido
        self.pasajeros = pasajeros
        self.ubicacion_actual = recorrido[0]
        
    def avanzar(self):
        index_actual = self.recorrido.index(self.ubicacion_actual)
        self.ubicacion_actual = self.recorrido[(index_actual + 1)]
        print(f"El minibus ha avanzado a la parada 🚏: {self.ubicacion_actual}")
        self.mostrar_estado()
        self.bajar_pasajeros()
        if self.ubicacion_actual == self.recorrido[-1]:
            self.recorrido.reverse()
            index_actual = 0
            print("🚩 El minibus dara la vuelta en esta parada")
            self.mostrar_estado()

    def subir_pasajero(self, pasajero):
        if pasajero.destino == self.ubicacion_actual:
            print(f"🚫 {pasajero.nombre}  Ya se encuentra en su destino: {pasajero.destino}\n")
            return
        if pasajero.destino not in self.recorrido:
            print(f"🚫 Su destino {pasajero.destino} no esta en la ruta\n")
            return
        self.pasajeros.append(pasajero)
        print(f"🧍 El pasajero {pasajero.nombre} a subido al minibus\n")

    def bajar_pasajeros(self):
        for pasajero in self.pasajeros[:]:
            if pasajero.destino == self.ubicacion_actual:
                self.pasajeros.remove(pasajero)
                print(f"🚶‍♂️ {pasajero.nombre} a bajado en su destino: {pasajero.destino}\n")
        
    def mostrar_estado(self):
        recorrido_str = " ---- ".join(self.recorrido)
        pasajeros_str = ", ".join([pasajero.nombre for pasajero in self.pasajeros])
        print(f"{recorrido_str}\n{' ' * (recorrido_str.index(self.ubicacion_actual))}🚐 {pasajeros_str} \n")

class Pasajero:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino
       

minibus = Minibus(12, ["Frutillar", "Circunvalacion", "America", "Ayacucho"], [])
juan = Pasajero("Juan", "Circunvalacion")
maria = Pasajero("Maria", "Circunvalacion")
ana = Pasajero("Ana", "Ayacucho")
pedro = Pasajero("Pedro", "Frutillar")

print("🚐 El minibus inicia su recorrido!!!\n")
minibus.mostrar_estado()
minibus.subir_pasajero(juan)
minibus.subir_pasajero(ana)
minibus.avanzar()
minibus.subir_pasajero(maria)
minibus.avanzar()
minibus.subir_pasajero(pedro)
minibus.avanzar()
minibus.avanzar()