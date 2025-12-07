class Helado:
    def __init__(self, envase):
        self.envase = envase
    
    def comer(self):
        print("Comiendo un helado")

class HeladoVainilla(Helado):
    def __init__(self, envase):
        super().__init__(envase)
        self.sabor = "vainilla"
        
    def __str__(self):
        return f"\n{self.sabor} 🍦 en {self.envase}"
    
    def comer(self):
        print("🍦 Comiendo un helado de vainilla")
        
class HeladoChocolate(Helado):
    def __init__(self, envase):
        super().__init__(envase)
        self.sabor = "chocolate"
        
    def __str__(self):
        return f"\n{self.sabor} 🍦 en {self.envase}"
    
    def comer(self):
        print("🍫 Comiendo un helado de chocolate")
        
class Maquina:
    def preparar(self):
        pass

class MaquinaVainilla(Maquina):
    def preparar(self, envase):
        return HeladoVainilla(envase)

class MaquinaChocolate(Maquina):
    def preparar(self, envase):
        return HeladoChocolate(envase)
    
class Encargado:
    def preparar_helado(self, tipo, envase):
        if tipo == "vainilla":
            return MaquinaVainilla().preparar(envase)
        if tipo == "chocolate":
            return MaquinaChocolate().preparar(envase)
        raise ValueError("❌ Helado no disponible. Intente de nuevo")

while True:
    print("🍨 Pedidos de Helado 🍨")
    print("1. Vainilla en Cono")
    print("2. Vainilla en Vaso")
    print("3. Chocolate en Cono")
    print("4. Chocolate en Vaso")
    print('Escribe "salir" para terminar.')
    pedido = input("💬 ¿Qué helado desea? (1-4/salir): ")
    if pedido.lower().strip() == "salir":
        print("🚶‍♂️ Saliendo de la heladería.")
        break
    try:
        encargado = Encargado()
        if pedido == "1":
            helado = encargado.preparar_helado("vainilla", "cono")
        elif pedido == "2":
            helado = encargado.preparar_helado("vainilla", "vaso")
        elif pedido == "3":
            helado = encargado.preparar_helado("chocolate", "cono")
        elif pedido == "4":
            helado = encargado.preparar_helado("chocolate", "vaso")
        else:
            print("❌ Opción no válida. Intente de nuevo.")
            continue
        print(helado)
        helado.comer()
    except ValueError as e:
        print(e)
