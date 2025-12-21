class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []
    
    def __str__(self):
        return self.nombre