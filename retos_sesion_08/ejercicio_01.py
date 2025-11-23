class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self._simplificar()
    
    def _maximo_comun_divisor(self, numerador, denominador):
        while denominador:
            numerador, denominador = denominador, numerador % denominador
        return numerador 
    
    def _simplificar(self):
        divisor_comun = self._maximo_comun_divisor(self.numerador, self.denominador)
        self.numerador //= divisor_comun
        self.denominador //= divisor_comun

    def __str__(self):
        if self.numerador == 0:
            return "0"
        if self.denominador == 1:
            return f"{self.numerador}"
        return f"{self.numerador}/{self.denominador}"
    
    def __add__(self, otro):
        nuevo_numerador = (self.numerador * otro.denominador) + \
        (otro.numerador * self.denominador)
        nuevo_denominador = self.denominador * otro.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __sub__(self, otro):        
        nuevo_numerador = (self.numerador * otro.denominador) - \
        (otro.numerador * self.denominador)
        nuevo_denominador = self.denominador * otro.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __mul__(self, otro):
        nuevo_numerador = self.numerador * otro.numerador
        nuevo_denominador = self.denominador * otro.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __truediv__(self, otro):
        nuevo_numerador = self.numerador * otro.denominador
        nuevo_denominador = self.denominador * otro.numerador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __eq__(self, otro):
        return (self.numerador * otro.denominador) == \
        (otro.numerador * self.denominador)
    
    def __lt__(self, otro):
        return (self.numerador * otro.denominador) < \
        (otro.numerador * self.denominador)
    
    def __gt__(self, otro):
        return (self.numerador * otro.denominador) > \
        (otro.numerador * self.denominador)
    
    def __ne__(self, otro):
        return not self.__eq__(otro)

# Ejemplo de uso
fraccion_uno = Fraccion(2, 4)
fraccion_dos = Fraccion(2, 4)
resultado = fraccion_uno + fraccion_dos
print(f"Resultado Suma: {resultado}")
resultado_resta = fraccion_uno - fraccion_dos
print(f"Resultado Resta: {resultado_resta}")
resultado_multiplicacion = fraccion_uno * fraccion_dos
print(f"Resultado Multiplicación: {resultado_multiplicacion}")
resultado_division = fraccion_uno / fraccion_dos
print(f"Resultado División: {resultado_division}")
print(fraccion_uno == fraccion_dos)  
print(fraccion_uno > fraccion_dos)   
print(fraccion_dos < fraccion_uno)   
print(fraccion_uno != fraccion_dos)