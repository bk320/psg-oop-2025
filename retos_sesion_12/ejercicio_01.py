import random

class DadosDeLaSuerte:
    """
    Clase que representa un juego de dados basado en la suerte.

    Attributes
    ----------
    suma_total : int
        Almacena el resultado del último lanzamiento.
    jugando : bool
        Estado que determina si el ciclo del juego continúa activo.
    """

    def __init__(self) -> None:
        """
        Inicializa los atributos del juego.
        """
        self.suma_total: int = 0
        self.jugando: bool = True

    def lanzar_dados(self) -> int:
        """
        Simula el lanzamiento de dos dados y calcula la suma.

        Returns
        -------
        int
            La suma de los valores obtenidos en los dos dados.
        """
        d1: int = random.randint(1, 6)
        d2: int = random.randint(1, 6)
        suma: int = d1 + d2
        print(f"\n🎲 Lanzamiento: {d1} + {d2} = {suma}")
        return suma

    def verificar_resultado(self, suma: int) -> str:
        """
        Verifica si el jugador ganó, perdió o debe continuar.

        Parameters
        ----------
        suma : int
            La suma total de los dados tras el lanzamiento.

        Returns
        -------
        str
            El estado del juego: 'gana', 'pierde' o 'continua'.
        """
        if suma in [7, 11]:
            return "gana"
        elif suma in [2, 3, 12]:
            return "pierde"
        return "continua"

    def jugar(self) -> None:
        """
        Inicia y gestiona el flujo principal del juego con validación de entrada.
        """
        print("--- Inicio del Juego: Dados de la Suerte ---")
        
        while self.jugando:
            self.suma_total = self.lanzar_dados()
            estado: str = self.verificar_resultado(self.suma_total)
            
            if estado == "gana":
                print("¡Resultado final: GANASTE! 🏆")
                self.jugando = False
            elif estado == "pierde":
                print("¡Resultado final: PERDISTE! ❌")
                self.jugando = False
            else:
                while True:
                    opcion: str = input("Resultado neutral. ¿Quieres volver a lanzar? (SI/NO): ").strip().upper()                    
                    if opcion == "SI":
                        break
                    elif opcion == "NO":
                        print(f"Te retiraste. Suma final: {self.suma_total}")
                        self.jugando = False
                        break
                    else:
                        print("⚠️ Opción no válida. Por favor, responde 'SI' o 'NO'.")
        print("\nGracias por jugar. ¡Vuelve pronto!")

if __name__ == "__main__":
    partida = DadosDeLaSuerte()
    partida.jugar()