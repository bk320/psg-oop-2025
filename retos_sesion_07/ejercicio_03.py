class Romano:
    romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    def __init__(self, simbolo_romano):
        self.simbolo_romano = simbolo_romano
    def __add__(self, romano):
        valor1 = self.__convertir_a_entero(self.simbolo_romano)
        valor2 = self.__convertir_a_entero(romano.simbolo_romano)
        suma = valor1 + valor2
        return Romano(self.__convertir_a_romano(suma))
    
    def __convertir_a_entero(self, simbolo):
        valor = 0
        for letra in simbolo:
            valor += self.romanos.get(letra, 0)
        return valor
    
    def __convertir_a_romano(self, numero):
        valor_romano = ""
        for simbolo, valor in sorted(self.romanos.items(), key=lambda x: x[1], reverse=True):
            while numero >= valor:
                valor_romano += simbolo
                numero -= valor
        return valor_romano
    
# Ejemplo de uso
num1 = Romano("XV")
num2 = Romano("V")
resultado = num1 + num2
print(f"La suma de {num1.simbolo_romano} y {num2.simbolo_romano} es {resultado.simbolo_romano}")