class Atleta:
    unica_comida = "hamburguesa"
    def __init__(self, nombre, energia, fuerza):
        self.nombre = nombre
        self.energia = energia
        self.fuerza = fuerza
    @classmethod
    def crear_atleta(cls, nombre):
        print("Un atleta ha nacido")
        return cls(nombre, 80, 25)
    
    def entrenar(self):
        if self.energia >= 20:
            self.fuerza = self.fuerza + 5
            self.energia = self.energia - 20
            print(f"{self.nombre} a ganado fuerza, pero a perdido enegia")
            print(f"Energia actual: {self.energia}, Fuerza actual: {self.fuerza}")
        else:
            print(f"{self.nombre} no tiene suficiente energia para entrenar")
    
    def descansar(self):
        self.energia = self.energia + 10
        print(f"{self.nombre} al descansar recupero energia")
        print(f"Energia actual: {self.energia}")
    
    def comer(self, comida):
        if comida == self.unica_comida:
            self.energia = self.energia + 15
            print(f"{self.nombre} comio una {comida} y recupero energia")
            print(f"Energia actual: {self.energia}")
        else:
            print(f"{self.nombre} no comia una {self.unica_comida}, no recupero energia")

atleta1 = Atleta.crear_atleta("Ricardo")
atleta2 = Atleta.crear_atleta("Roberto")
atleta1.entrenar()
atleta2.entrenar()
atleta1.descansar()
atleta2.descansar()
atleta1.comer("hamburguesa")
atleta2.comer("manzana")