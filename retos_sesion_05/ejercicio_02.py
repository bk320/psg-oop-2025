class Nadador:
    
    def nadar(self):
        print("Me desplazo por el agua")

class Volador:

    def volar(self):
        print("Me desplazo por el aire")
        
class Pez(Nadador):

    def mostrar(self):
        print("\nHola soy un Pez de:")
        if isinstance (self, Nadador):
            print("Tipo nadador")

class Pajaro(Volador):

    def mostrar(self):
        print("\nHola soy un Pájaro de:")
        if isinstance (self, Volador):
            print("Tipo volador")

class Pato(Nadador, Volador):

    def mostrar(self):
        print("\nHola soy un Pato de:")
        if isinstance (self, Nadador):
            print("Tipo nadador")
        if isinstance (self, Volador):
            print("Tipo volador")


# Ejemplo de uso
pez = Pez()
pez.mostrar()
pez.nadar()

pajaro = Pajaro()
pajaro.mostrar()
pajaro.volar()

pato = Pato()
pato.mostrar()
pato.nadar()
pato.volar()