edad: int = 30  
nombre: str = "Jhon" 
altura: float = 1.75
activo: bool = True
print(type(edad))  # <class 'int'>
print(type(nombre))  # <class 'str'>
print(type(altura))  # <class 'float'>
print(type(activo))  # <class 'bool'>

numeros: list[int] = []
nombres: dict[str, str] = {}  
tuplas: tuple[int, str] = ()
print(type(numeros))  # <class 'list'>
print(type(nombres))  # <class 'dict'>
print(type(tuplas))  # <class 'tuple'>

def sumar(a: int, b: int) -> int:
    return a + b

def cuadrados(numeros: list[int]) -> list[int]:
    return [n ** 2 for n in numeros]
numeros = cuadrados([2,4,6])
print (numeros)

class Persona:
    especie: str = "Homo sapiens"
    def __init__(self, nombre: str, edad: int):
        self.nombre: str = nombre
        self.edad: int = edad
        
from typing import List
def cuadrados(numeros: List[int]) -> List[int]:
    return [n ** 2 for n in numeros]
numeros = cuadrados([2, 4, 6])
print(numeros)

