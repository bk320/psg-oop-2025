class Persona:
    def __init__(self, nombre: str):
        self.nombre: str = nombre
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")
jhon = Persona("Jhon")
jhon.saludar()

class Persona:
    """Clase que representa a una persona."""
    def __init__(self, nombre: str):
        """Inicializa una nueva instancia de la clase Persona.
        
        Args:
            nombre (str): El nombre de la persona.
        """
        self.nombre: str = nombre

    def saludar(self):
        """Imprime un saludo con el nombre de la persona."""
        print(f"Hola, mi nombre es {self.nombre}")
jhon = Persona("Jhon")
jhon.saludar()
