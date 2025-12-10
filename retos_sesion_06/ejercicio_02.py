class Oficina:
    def __init__(self, codigo_oficina, telefono):
        self.codigo_oficina = codigo_oficina
        self.telefono = telefono

    def mostrar_info(self, numero_piso):
        print(f"------>💼  Oficina: {numero_piso}{self.codigo_oficina}, Teléfono: {self.telefono}")
class Departamento:
    def __init__(self, numero_departamento, inquilinos):
        self.numero_departamento = numero_departamento
        self.inquilinos = inquilinos

    def mostrar_info(self, numero_piso):
        print(f"------>🏠  Departamento: {numero_piso}{self.numero_departamento}, Inquilinos: {', '.join(self.inquilinos)}")

class Piso:
    def __init__(self, numero_piso):
        self.numero_piso = numero_piso
        self.oficinas = []
        self.departamentos = []
        
    def agregar_oficina(self, letra_oficina, telefono):
        oficina = Oficina(letra_oficina, telefono)
        self.oficinas.append(oficina)
        return oficina
    
    def agregar_departamento(self, numero_departamento, inquilinos):
        departamento = Departamento(numero_departamento, inquilinos)
        self.departamentos.append(departamento)
        return departamento

    def mostrar_info(self):
        print(f"🏙️ -->Piso: {self.numero_piso}")
        for oficina in self.oficinas:
            oficina.mostrar_info(self.numero_piso)
        for departamento in self.departamentos:
            departamento.mostrar_info(self.numero_piso)

class Edificio:
    def __init__(self, direccion, nombre):
        self.direccion = direccion
        self.nombre = nombre
        piso_uno = Piso(1)
        piso_dos = Piso(2)
        piso_tres = Piso(3)
        self.pisos = [piso_uno, piso_dos, piso_tres]

    def mostrar_info(self):
        print(f"🏢  Edificio: {self.nombre}, Dirección: {self.direccion}")
        for piso in self.pisos:
            piso.mostrar_info()
            
    def agregar_oficina_a_piso(self, numero_piso, letra_oficina, telefono):
        for piso in self.pisos:
            if piso.numero_piso == numero_piso:
                return piso.agregar_oficina(letra_oficina, telefono)
        return None
    
    def agregar_departamento_a_piso(self, numero_piso, numero_departamento, inquilinos):
        for piso in self.pisos:
            if piso.numero_piso == numero_piso:
                return piso.agregar_departamento(numero_departamento, inquilinos)
        return None

edificio_alameda = Edificio("Av. 16 de Julio", "Edificio Alameda")

edificio_alameda.agregar_oficina_a_piso(1, "A", "77990664")
edificio_alameda.agregar_oficina_a_piso(1, "B", "77990665")
edificio_alameda.agregar_departamento_a_piso(1, "01", ["Alice", "Rabbit"])
edificio_alameda.agregar_departamento_a_piso(1, "02", ["Charlie"])

edificio_alameda.agregar_oficina_a_piso(2, "C", "77990666")
edificio_alameda.agregar_oficina_a_piso(2, "D", "77990667")
edificio_alameda.agregar_departamento_a_piso(2, "03", ["Genji", "Hanzo"])
edificio_alameda.agregar_departamento_a_piso(2, "04", ["Roberto"])

edificio_alameda.agregar_oficina_a_piso(3, "E", "77990668")
edificio_alameda.agregar_departamento_a_piso(3, "05", ["Wili", "Elmo"])
edificio_alameda.agregar_departamento_a_piso(3, "06", ["Patricio", "Bob"])
edificio_alameda.agregar_departamento_a_piso(3, "07", ["Rocky"])

edificio_alameda.mostrar_info()