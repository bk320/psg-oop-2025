class Oficina:
    def __init__(self, nombre_oficina, telefono):
        self.nombre_oficina = nombre_oficina
        self.telefono = telefono

    def mostrar_info(self, numero_piso):
        print(f"------>💼  Oficina: {numero_piso}{self.nombre_oficina}, Teléfono: {self.telefono}")

class Departamento:
    def __init__(self, numero_departamento, inquilinos):
        self.numero_departamento = numero_departamento
        self.inquilinos = inquilinos

    def mostrar_info(self, numero_piso):
        print(f"------>🏠  Departamento: {numero_piso}{self.numero_departamento}, Inquilinos: {', '.join(self.inquilinos)}")

class Piso:
    def __init__(self, numero_piso, oficinas, departamentos):
        self.numero_piso = numero_piso
        self.oficinas = oficinas
        self.departamentos = departamentos

    def mostrar_info(self):
        print(f"-->Piso: {self.numero_piso}")
        for oficina in self.oficinas:
            oficina.mostrar_info(self.numero_piso)
        for departamento in self.departamentos:
            departamento.mostrar_info(self.numero_piso)

class Edificio:
    def __init__(self, direccion, nombre, pisos):
        self.direccion = direccion
        self.nombre = nombre
        self.pisos = pisos

    def mostrar_info(self):
        print(f"🏢  Edificio: {self.nombre}, Dirección: {self.direccion}")
        for piso in self.pisos:
            piso.mostrar_info()
    
departamento_1 = Departamento("01", ["Alice", "Bob"])
departamento_2 = Departamento("02", ["Charlie"])
departamento_3 = Departamento("03", ["David", "Hanzo"])
departamento_4 = Departamento("04", ["Frank"])
departamento_5 = Departamento("05", ["Wili", "Heidi"])
departamento_6 = Departamento("06", ["Patricio", "Harold"])
departamento_7 = Departamento("07", ["Rocky"])
oficina_1 = Oficina("A", "77990664")
oficina_2 = Oficina("B", "77990665")
oficina_3 = Oficina("C", "77990666")
oficina_4 = Oficina("D", "77990667")
oficina_5 = Oficina("E", "77990668")
piso_1 = Piso(1, [oficina_1, oficina_2], [departamento_1, departamento_2])
piso_2 = Piso(2, [oficina_3], [departamento_3, departamento_4])
piso_3 = Piso(3, [oficina_4, oficina_5], [departamento_5, departamento_6, departamento_7])
edificio_1 = Edificio("Av. 16 de Julio", "Edificio Alameda", [piso_1, piso_2, piso_3])

edificio_1.mostrar_info()