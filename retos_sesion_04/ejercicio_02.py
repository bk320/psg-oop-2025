class celula:
    def __init__ (self, adn, tipo_celula, energia):
        self._adn = adn
        self.tipo_celula = tipo_celula
        self.__energia = energia
    @property
    def adn(self):
        return self._adn
    
    def comer(self):
        self.__energia += 10
        print(f"la celula se ha alimentado, nivel de energía: {self.__energia}")
        
    def dividir(self):
        if self.__energia >= 20:
            self.__energia -= 20
            print("La célula se ha dividido, nivel de energía restante:", self.__energia)
        else:
            print("Energía insuficiente para dividirse.")
        
# Implementando la clase
celula1 = celula("AGCTTAGC", "Eucariota", 35)
print(f"ADN: {celula1.adn}")
print(f"Tipo de célula: {celula1.tipo_celula}")
celula1.tipo_celula = "Procariota"
print(f"Nuevo tipo de célula: {celula1.tipo_celula}")
celula1.comer()
celula1.dividir()
try:
    print(f"Energía: {celula1.__energia}")
except AttributeError as e:
    print(f"Error: {e}")
