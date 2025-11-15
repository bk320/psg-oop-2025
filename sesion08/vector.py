# Definición
class Vector:
    def __init__(self, x, y):  # Constructor
        self.x = float(x)
        self.y = float(y)
    def __str__(self):
        return f"[{self.x}, {self.y}]"
    def magnitud(self):
        return abs(self.x) + abs(self.y)
    def __int__(self):
        return int(self.magnitud())
    def __float__(self):
        return float(self.magnitud())
    def __bool__(self):  # Método de conversión a booleano
        return self.magnitud() > 0
# Uso
a = Vector(3.1, -4.1)
print(a)
magnitud = int(a) 
print(magnitud) 
magnitud = float(a) 
print(magnitud) 
booleano = bool(a)
print(booleano)  # Conversión a booleano