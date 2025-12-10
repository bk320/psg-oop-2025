class Animal:
    origen = "feral"
    def __init__ (self, especie, tipo_animal, lugar_hallazgo):
        self.especie = especie
        self.tipo_animal = tipo_animal
        self.lugar_hallazgo = lugar_hallazgo

print("Animales encontrados...")
tigre = Animal("Tigre", "mamifero", "selva")
lobo = Animal("Lobo", "mamifero", "bosque")
print("Animal 1: ", tigre.origen, tigre.especie, tigre.tipo_animal, tigre.lugar_hallazgo)
print("Animal 2: ", lobo.origen, lobo.especie, lobo.tipo_animal, lobo.lugar_hallazgo)
reptil= Animal("Cocodrilo", "reptil", "río")
print("Animal 3: ", reptil.origen, reptil.especie, reptil.tipo_animal, reptil.lugar_hallazgo)
ave= Animal("Aguila", "ave", "montaña")
print("Animal 4: ", ave.origen, ave.especie, ave.tipo_animal, ave.lugar_hallazgo)