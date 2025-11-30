import random

class PiedraPapelTijera:
    __instance = None
    __iniciado = False
    __puntaje_jugador = 0
    __eleccion_computadora = ""
    __puntaje_computadora = 0
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def iniciar_partida(self):
        if self.__iniciado:
            print("💢 El juego ya está en curso.")
            return
        formas = ["Piedra", "Papel", "Tijera"]
        self.__eleccion_computadora = random.choice(formas)
        self.__iniciado = True

    def finalizar_juego(self):
        print("❗ Partida finalizada.")
        self.__iniciado = False
        
    def estado_juego(self):
        return self.__iniciado
    
    def eleccion_jugador(self, eleccion, nombre):
        print(f"🕹️ {nombre} eligio: {eleccion}")
        print(f"🤖 La computadora eligio: {self.__eleccion_computadora}")
        if eleccion == self.__eleccion_computadora:
            print("\n\n🔄 Empate!")
        elif (eleccion == "Piedra" and self.__eleccion_computadora == "Tijera") or \
             (eleccion == "Papel" and self.__eleccion_computadora == "Piedra") or \
             (eleccion == "Tijera" and self.__eleccion_computadora == "Papel"):
            print("\n\n🎉 ¡Ganaste! 🎉")
            self.__puntaje_jugador += 1
        else:
            print("\n\n🤖 ¡La computadora gana! 🤖")
            self.__puntaje_computadora += 1
        return False
    
    def mostrar_score(self, nombre):
        print("="*60)
        print("🏁 Score")
        while True:
            print(f"\n🕹️ {nombre}: {self.__puntaje_jugador} puntos")
            print(f"🤖 Computadora: {self.__puntaje_computadora} puntos\n")
            print("="*60)
            continuar = input("salir al menú principal? (s/n): ")
            if continuar.lower() == "s":
                break
            
    def reiniciar_juego(self):
        print("🔄 Reiniciando el juego...")
        self.__puntaje_jugador = 0
        self.__puntaje_computadora = 0


def seleccion_forma():
    while True:
        print("="*60)
        print("Selecciona tu opcion:")
        print("\n1. Piedra")
        print("2. Papel")
        print("3. Tijera\n")
        print("="*60)
        eleccion = input("Elige una opcion o 's' para salir: ")
        if eleccion == "1":
            return "Piedra"
        elif eleccion == "2":
            return "Papel"
        elif eleccion == "3":
            return "Tijera"
        elif eleccion.lower() == "s":
            return "salir"
        else:
            print("💢 Opción no válida. Inténtalo de nuevo.")

juego = PiedraPapelTijera()
nombre = input("💬 Tu nombre: ")           
while True:
    print("="*60)
    print(f"✊ Bienvenido: {nombre} \n A Piedra, Papel o Tijera ✋")
    print("1. Iniciar una nueva partida")
    print("2. Mostrar puntajes")
    print("3. Reiniciar el juego")
    print("4. Salir")
    print("="*60)
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        juego.iniciar_partida()
        while juego.estado_juego():
            eleccion = seleccion_forma()
            if eleccion.lower() == "salir":
                juego.finalizar_juego()
            else:
                juego.eleccion_jugador(eleccion, nombre)
                juego.finalizar_juego()
    elif opcion == "2":
        juego.mostrar_score(nombre)
    elif opcion == "3":
        juego.reiniciar_juego()
    elif opcion == "4":
        print("¡Gracias por jugar! ¡Hasta luego!")
        break
    else:
        print("💢 Opción no válida. Inténtalo de nuevo.")