class Nadador:
    
    def nadar(self):
        print("Se esta desplazando por agua")
    def mostrar(self):
        print("Tipo Nadador")

class Volador:

    def volar(self):
        print("Se esta desplazando por el aire")
    def mostrar(self):
        print("Tipo Volador")
        
class Pez(Nadador):

    def mostrar(self):
        print("Hola soy un Pez de tipo:")
        super().mostrar()

class Pajaro(Volador):

    def mostrar(self):
        print("Hola soy un Pájaro de tipo:")
        super().mostrar()

class Pato(Nadador, Volador):

    def mostrar(self):
        print("Hola soy un Pato de tipos:")
        Nadador.mostrar(self)
        Volador.mostrar(self)

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