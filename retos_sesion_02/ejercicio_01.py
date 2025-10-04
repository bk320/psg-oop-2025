class Animal:
    origen = "feral"
    def __init__ (self, especie, tipo):
        self.especie = especie
        self.tipo = tipo

print("Animales encontrados...")
mamifero1 = Animal("Tigre", "mamífero")
mamifero2 = Animal("Lobo", "mamífero")
print("Animal 1: ", mamifero1.origen, mamifero1.especie, mamifero1.tipo)
print("Animal 2: ", mamifero2.origen, mamifero2.especie, mamifero2.tipo)
reptil1 = Animal("Cocodrilo", "reptil")
print("Animal 3: ", reptil1.origen, reptil1.especie, reptil1.tipo)
ave1 = Animal("Águila", "ave")
print("Animal 4: ", ave1.origen, ave1.especie, ave1.tipo)