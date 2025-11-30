class BeatBox:
    __instance = None
    __pista_audio = ""
    __nivel_volumen = 30
    __efecto_sonido = ""
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def seleccionar_pista(self, pista):
        self.__pista_audio = pista
        print(f"Pista seleccionada: {self.__pista_audio}")
    
    def ajustar_volumen(self, nivel):
        if nivel >= 0 and nivel <= 100:   
            self.__nivel_volumen = nivel
            print(f"\nNivel de volumen ajustado a: {self.__nivel_volumen}")
        else:
            print("💢 Nivel de volumen debe estar entre 0 y 100.")
    
    def aplicar_efecto(self, efecto):
        self.__efecto_sonido = efecto
        print(f"Efecto de sonido aplicado: {self.__efecto_sonido}")
    
    def mostrar_estado(self):
        while True:
            print("\n\n==================================")
            print("🎵 Estado del BeatBox 🎵")
            print(f"Pista de audio: {self.__pista_audio}")
            print(f"Nivel de volumen: {self.__nivel_volumen}")
            print(f"Efecto de sonido: {self.__efecto_sonido}")
            print("===================================")
            salir = input("¿Desea salir del estado actual? (s/n): ")
            if salir.lower() == "s":
                break
    

def efecto_sonido():
    while True:
        print("\n\n===================================")
        print("Seleccione un efecto de sonido:")
        print("1. Eco")
        print("2. Reverb")
        print("3. Distorsión")
        print("=======================================")
        eleccion = input("si no desea aplicar efecto, presione cualquier otra tecla: ")
        if eleccion == "1":
            return "Eco"
        elif eleccion == "2":
            return "Reverb"
        elif eleccion == "3":
            return "Distorsión"
        else:
            return ""
            
            
while True:
    print("\n\n==================================")
    print("🎧 Bienvenido a la Consola de BeatBox 🎧")
    print("1. Ingresar el nombre de la pista de audio")
    print("2. Ajustar volumen (subir o bajar)")
    print("3. Aplicar efecto de sonido")
    print("4. Mostrar estado actual")
    print("5. Salir")
    print("==================================")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        pista = input("Ingrese el nombre de la pista de audio: ")
        BeatBox().seleccionar_pista(pista)
    elif opcion == "2":
        try:
            nivel = int(input("Ingrese el nivel de volumen (0-100): "))
            BeatBox().ajustar_volumen(nivel)
        except ValueError:
            print("💢 Por favor, ingrese un número válido para el nivel de volumen.")
    elif opcion == "3":
        efecto = efecto_sonido()
        BeatBox().aplicar_efecto(efecto)
    elif opcion == "4":
        BeatBox().mostrar_estado()
    elif opcion == "5":
        print("Saliendo de la Consola de BeatBox. ¡Hasta luego!")
        break
    else:
        print("💢 Opción no válida. Por favor, intente de nuevo.")