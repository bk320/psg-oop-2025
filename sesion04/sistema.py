# Definiendo la clase
class SistemaOperativo:
    def __init__(self, nombre, fondo_pantalla, reloj):
        self.nombre = nombre 
        self.fondo_pantalla = fondo_pantalla 
        self._reloj = reloj # Protegido
        self.__bateria = 60 # Privado
        self.__pin = '0000'  # Privado
    def cambiar_fondo_pantalla(self, nuevo_fondo):
        self.fondo_pantalla = nuevo_fondo
        print(f"Nuevo fondo: {self.fondo_pantalla}")
        return self.fondo_pantalla
    def ver_hora(self):
        print(f"La hora actual es: {self._reloj}")
        return self._reloj
    def estado_bateria(self):
        print(f"Nivel de batería: {self.__bateria}%")
        return self.__bateria
    def cargador(self, cantidad):
        print("🔌 Cargador conectado.")
        self.__bateria += cantidad
        print(f"Batería cargada a: {self.__bateria}%")
        print("🔌 Cargador desconectado.")
    def cambiar_pin(self, nuevo_pin):
        self.__pin = nuevo_pin
        print("PIN cambiado exitosamente.")
# Implementando la clase
so = SistemaOperativo("PyPhoneOS", "gatitos.jpg", "12:00 PM")
print(f"Fondo de pantalla: {so.fondo_pantalla}")
so.cambiar_fondo_pantalla("perritos.jpg")
so.fondo_pantalla = "paisajes.jpg"
print(f"Fondo de pantalla: {so.fondo_pantalla}")
so.ver_hora()
print(f"Reloj: {so._reloj}")  # Posible, pero no recomendado
so.estado_bateria()
so.cargador(20)
so.estado_bateria()
so.cambiar_pin('5678') 
try:
    print(f"Batería: {so.__bateria}")  # Error
except AttributeError as e:
    print(f"Error: {e}")