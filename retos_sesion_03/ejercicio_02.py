class Cocinero:
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
            self.productividad += 1
        else:
            print(f"{self.nombre} no posee la receta de {receta}")
    
    @staticmethod
    def productividad_total(cocineros):
        total = 0
        for cocinero in cocineros:
            total += cocinero.productividad
        print(f"La productividad total de los cocineros es: {total}")
    
beto = Cocinero.crear_cocinero("Beto", ["harina", "agua", "sal", "tomate", "queso"])
ron = Cocinero.crear_cocinero("Ron", ["harina", "agua", "chocolate", "sal"])
richard = Cocinero.crear_cocinero("Richard", ["agua", "harina"])

beto.cocinar("pizza")
beto.cocinar("pan")

ron.cocinar("galleta")

richard.cocinar("pan")
richard.cocinar("pizza")
richard.cocinar("ensalada")

Cocinero.productividad_total([beto, ron, richard])