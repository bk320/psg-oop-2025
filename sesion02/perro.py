class Perro:
    especie = "canino"
    tipo = "mamífero"
    habitat = "terrestre"
    def __init__(self, nombre, edad, genero, raza, vacunado, propietario):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.raza = raza
        self.vacunado = vacunado
        self.propietario = propietario

canito = Perro("Canito", 3, "Macho", "Golden retriever", True, "Carlos")
pluto = Perro("Pluto", 5, "Macho", "Beagle", False, "Richard")

# Mostrar atributos
print("Canito: ", canito.especie, canito.tipo, canito.habitat)
print(canito.nombre)
print(canito.edad)
print(canito.genero)
print(canito.raza)
print(canito.vacunado)
print(canito.propietario)
print("Pluto: ", pluto.especie, pluto.tipo, pluto.habitat)
print(pluto.nombre)
print(pluto.edad)
print(pluto.genero)
print(pluto.raza)
print(pluto.vacunado)
print(pluto.propietario)
print("Perro es: ", Perro.tipo, "Especie: ", Perro.especie, "Habitat: ", Perro.habitat)