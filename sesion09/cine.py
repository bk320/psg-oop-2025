class Sala:
    __instancia = None
    titulo = ""
    reproducciendo = False
    clientes = []

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia
    def iniciar(self, titulo):
        if self.reproducciendo:
            print(f"Acualmente se esta reproduciendo una pelicula {self.titulo}.")
            return
        self.titulo = titulo
        self.reproducciendo = True
        print(f"Iniciando la pelicula: {self.titulo}")
    
    def unirse(self, cliente):
        self.clientes.append(cliente)
        print(f"{cliente} se ha unido a la sala.")
    
    def estado(self):
        estado = "En reproducción" if self.reproducciendo else "Detenida"
        print(f"🎥 Película: {self.titulo} | Estado: {estado}")
        
    def listar(self):
        print(f"👥 Clientes en la sala: {len(self.clientes)}")
        for cliente in self.clientes:
            print(f"- {cliente}")
    
    def finalizar(self):
        print("❗ Película finalizada.")
        self.reproducciendo = False

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return self.nombre
    
    def unirse(self):
        Sala().unirse(self)
        
while True:
    print("==================================")
    print("🎬 Bienvenido al Cine Virtual 🎬")
    print("1. Iniciar Película")
    print("2. Unirse a la Sala")
    print("3. Estado de la Sala")
    print("4. Listar Clientes")
    print("5. Finalizar Película")
    print("6. Salir")
    print("==================================")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        titulo = input("Ingrese el título de la película: ")
        Sala().iniciar(titulo)
    elif opcion == "2":
        nombre = input("Ingrese su nombre: ")
        cliente = Cliente(nombre)
        cliente.unirse()
    elif opcion == "3":
        Sala().estado()
    elif opcion == "4":
        Sala().listar()
    elif opcion == "5":
        Sala().finalizar()
    elif opcion == "6":
        print("Saliendo del Cine Virtual. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")