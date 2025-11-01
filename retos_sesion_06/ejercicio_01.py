class Minibus:
    def __init__(self, numero_ruta, recorrido, pasajeros):
        self.numero_ruta = numero_ruta
        self.recorrido = recorrido
        self.pasajeros = pasajeros
        self.ubicacion_actual = recorrido[0]
        
    def avanzar(self):
        index_actual = self.recorrido.index(self.ubicacion_actual)
        if index_actual == len(self.recorrido) - 1:
            self.recorrido.reverse()
            index_actual = 0
        self.ubicacion_actual = self.recorrido[(index_actual + 1)]
        print(f"El minibus ha avanzado en su recorrido a la parada: {self.ubicacion_actual}")
        for pasajero in self.pasajeros[:]:
            self.bajar_pasajero(pasajero)
        
    
    def subir_pasajero(self, pasajero):
        if pasajero.destino in self.recorrido:
            if pasajero.destino == self.ubicacion_actual:
                print(f"Ya se encuentra en su destino: {pasajero.destino}, no puede subir al minibus")
            else:
                self.pasajeros.append(pasajero)
                print(f"El pasajero {pasajero.nombre} ha subido al minibus")
        else:
            print(f"Disculpe {pasajero.nombre}, su destino {pasajero.destino} no está en el recorrido del minibus")

    def bajar_pasajero(self, pasajero):
        if pasajero.destino == self.ubicacion_actual:
            self.pasajeros.remove(pasajero)
            print(f"El pasajero {pasajero.nombre} ha bajado en su destino: {pasajero.destino}")
        
    def mostrar_estado(self):
        recorrido_str = " ---- ".join(self.recorrido)
        pasajeros_str = ", ".join([pasajero.nombre for pasajero in self.pasajeros])
        print(f"{recorrido_str}\n{' ' * (recorrido_str.index(self.ubicacion_actual))}🚐 {pasajeros_str} \n")
class Pasajero:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino
       

Minibus_1 = Minibus(12, ["Frutillar", "Circunvalacion", "America", "Ayacucho"], [])
Pasajero_1 = Pasajero("Juan", "Circunvalacion")
Pasajero_2 = Pasajero("Maria", "Circunvalacion")
Pasajero_3 = Pasajero("Carlos", "Circunvalacion")
Pasajero_4 = Pasajero("Luis", "Ayacucho")
Pasajero_5 = Pasajero("Ana", "Vaticano")
Pasajero_6 = Pasajero("Pedro", "Frutillar")

Minibus_1.mostrar_estado()
Minibus_1.subir_pasajero(Pasajero_1)
Minibus_1.subir_pasajero(Pasajero_5)
Minibus_1.mostrar_estado()
Minibus_1.avanzar()
Minibus_1.mostrar_estado()

Minibus_1.subir_pasajero(Pasajero_2)
Minibus_1.avanzar()
Minibus_1.mostrar_estado()
Minibus_1.subir_pasajero(Pasajero_3)
Minibus_1.avanzar()
Minibus_1.mostrar_estado()
Minibus_1.subir_pasajero(Pasajero_6)
Minibus_1.avanzar()
Minibus_1.mostrar_estado()
Minibus_1.subir_pasajero(Pasajero_4)
Minibus_1.avanzar()
Minibus_1.mostrar_estado()