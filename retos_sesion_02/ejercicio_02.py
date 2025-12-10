class Vino:
    def __init__ (self, nombre_vino, tipo_vino, cepa, anio_produccion):
        self.nombre_vino = nombre_vino
        self.tipo_vino = tipo_vino
        self.cepa = cepa
        self.anio_produccion = anio_produccion
class Queso:
    def __init__ (self, nombre_queso, variedad_queso, edad_queso, lleva_sal):
        self.nombre_queso = nombre_queso
        self.variedad_queso = variedad_queso
        self.edad_queso = edad_queso
        self.lleva_sal = lleva_sal
        
print("Vinos en inventario:")
vino_uno = Vino("Chateau Margaux", "Tinto", "Cabernet Sauvignon", 1990)
vino_dos = Vino("Chianti", "Tinto", "Sangiovese", 1991)
vino_tres = Vino("Dom Pérignon", "Espumoso", "Chardonnay", 1962)
vino_cuatro = Vino("Merlot", "Tinto", "Merlot", 2004)
print("Vino 1: ", vino_uno.nombre_vino, vino_uno.tipo_vino, vino_uno.cepa, \
    vino_uno.anio_produccion)
print("Vino 2: ", vino_dos.nombre_vino, vino_dos.tipo_vino, vino_dos.cepa, \
    vino_dos.anio_produccion)
print("Vino 3: ", vino_tres.nombre_vino, vino_tres.tipo_vino, vino_tres.cepa, \
    vino_tres.anio_produccion)
print("Vino 4: ", vino_cuatro.nombre_vino, vino_cuatro.tipo_vino, vino_cuatro.cepa, \
    vino_cuatro.anio_produccion)

print("Quesos en inventario:")
queso_uno = Queso("Roquefort", "Azul", 5, True)
queso_dos = Queso("Parmesano", "Duro", 24, True)
queso_tres = Queso("Brie", "Blando", 2, False)
print("Queso 1: ", queso_uno.nombre_queso, queso_uno.variedad_queso, \
    queso_uno.edad_queso, queso_uno.lleva_sal)
print("Queso 2: ", queso_dos.nombre_queso, queso_dos.variedad_queso, \
    queso_dos.edad_queso, queso_dos.lleva_sal)
print("Queso 3: ", queso_tres.nombre_queso, queso_tres.variedad_queso, \
    queso_tres.edad_queso, queso_tres.lleva_sal)