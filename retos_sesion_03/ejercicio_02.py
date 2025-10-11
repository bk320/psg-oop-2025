class Cocinero:
    productividad_total = 0
    recetas = {
        'pan': ['harina', 'agua'],
        'pizza': ['harina', 'agua', 'sal', 'tomate', 'queso'],
        'galleta': ['harina', 'agua', 'sal', 'chocolate']
    }
    def __init__(self, nombre, ingredientes):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.productividad = 0

    @classmethod
    def crear_cocinero(cls, nombre, ingredientes):
        print(f"Comienza el turno del cocinero {nombre}")
        return cls(nombre, ingredientes)
    
    def cocinar(self, receta):
        if receta in self.recetas:
            for ingrediente in self.recetas[receta]:
                if ingrediente not in self.ingredientes:
                    print(f"{self.nombre} no tiene los ingredientes para cocinar {receta}")
                    return
            print(f"{self.nombre} ha cocinado una {receta}")
            self.productividad = self.productividad + 1
            Cocinero.productividad_total = Cocinero.productividad_total + 1
        else:
            print(f"{self.nombre} no posee la receta de {receta}")
    
    @staticmethod
    def mostrar_productividad_total():
        print(f"La productividad total de los cocineros es: {Cocinero.productividad_total}")
    
cocinero1 = Cocinero.crear_cocinero("Beto", ["harina", "agua", "sal", "tomate", "queso"])
cocinero2 = Cocinero.crear_cocinero("Ron", ["harina", "agua", "chocolate", "sal"])
cocinero3 = Cocinero.crear_cocinero("Richard", ["agua", "harina"])

cocinero1.cocinar("pizza")
cocinero1.cocinar("pan")
cocinero2.cocinar("galleta")
cocinero3.cocinar("pan")
cocinero3.cocinar("pizza")
cocinero3.cocinar("ensalada")

Cocinero.mostrar_productividad_total()
