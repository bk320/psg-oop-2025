class Vino:
    def __init__ (self, nombre, tipo, cepa, año):
        self.nombre = nombre
        self.tipo = tipo
        self.cepa = cepa
        self.año = año

class Queso:
    def __init__ (self, nombre, variedad, edad, sal):
        self.nombre = nombre
        self.variedad = variedad
        self.edad = edad
        self.sal = sal
        
print("Vinos en inventario:")
vino1 = Vino("Chateau Margaux", "Tinto", "Cabernet Sauvignon", 1990)
vino2 = Vino("Chianti", "Tinto", "Sangiovese", 1991)
vino3 = Vino("Dom Pérignon", "Espumoso", "Chardonnay", 1962)
vino4 = Vino("Merlot", "Tinto", "Merlot", 2004)
print("Vino 1: ", vino1.nombre, vino1.tipo, vino1.cepa, vino1.año)
print("Vino 2: ", vino2.nombre, vino2.tipo, vino2.cepa, vino2.año)
print("Vino 3: ", vino3.nombre, vino3.tipo, vino3.cepa, vino3.año)
print("Vino 4: ", vino4.nombre, vino4.tipo, vino4.cepa, vino4.año)

print("Quesos en inventario:")
queso1 = Queso("Roquefort", "Azul", 5, True)
queso2 = Queso("Parmesano", "Duro", 24, True)
queso3 = Queso("Brie", "Blando", 2, False)
print("Queso 1: ", queso1.nombre, queso1.variedad, queso1.edad, queso1.sal)
print("Queso 2: ", queso2.nombre, queso2.variedad, queso2.edad, queso2.sal)
print("Queso 3: ", queso3.nombre, queso3.variedad, queso3.edad, queso3.sal)