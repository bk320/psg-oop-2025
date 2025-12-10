class Celula:
    def __init__ (self, adn, tipo_celula, nivel_energia):
        self._adn = adn
        self.tipo_celula = tipo_celula
        self.__nivel_energia = nivel_energia

    @property
    def adn(self):
        return self._adn
    
    def comer(self):
        self.__nivel_energia += 10
        print(f"la celula se ha alimentado, nivel de energia: {self.__nivel_energia}")
        
    def dividir(self):
        if self.__nivel_energia >= 20:
            self.__nivel_energia -= 20
            print("La celula se ha dividido, nivel de energia restante:", self.__nivel_energia)
        else:
            print("Energia insuficiente para dividirse.")
        
# Implementando la clase
celula = Celula("AGCTTAGC", "Eucariota", 35)
print(f"ADN: {celula.adn}")
print(f"Tipo de celula: {celula.tipo_celula}")
celula.tipo_celula = "Procariota"
print(f"Nuevo tipo de celula: {celula.tipo_celula}")
celula.comer()
celula.dividir()
try:
    print(f"Energía: {celula.__nivel_energia}")
except AttributeError as e:
    print(f"Error: {e}")
