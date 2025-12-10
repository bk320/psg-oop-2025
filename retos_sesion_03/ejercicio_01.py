class Atleta:
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
            self.fuerza += 5
            self.energia -= 20
            print(f"{self.nombre} a ganado fuerza, pero a perdido enegia")
            print(f"Energia actual: {self.energia}, Fuerza actual: {self.fuerza}")
        else:
            print(f"{self.nombre} no tiene suficiente energia para entrenar")
    
    def descansar(self):
        self.energia += 10
        print(f"{self.nombre} al descansar recupero energia")
        print(f"Energia actual: {self.energia}")
    
    def comer(self, comida):
        if comida == "hamburguesa":
            self.energia += 15
            print(f"{self.nombre} comio una {comida} y recupero energia")
            print(f"Energia actual: {self.energia}")
        else:
            print(f"{self.nombre} solo come hamburguesas para recuperar energia")


atleta_uno = Atleta.crear_atleta("Ricardo")
atleta_dos = Atleta.crear_atleta("Roberto")

atleta_uno.entrenar()
atleta_dos.entrenar()

atleta_uno.descansar()
atleta_dos.descansar()

atleta_uno.comer("hamburguesa")
atleta_dos.comer("manzana")