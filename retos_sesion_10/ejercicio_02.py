DRAGON = "dragon"
ZOMBI = "zombi"
VAMPIRO = "vampiro"
REGLAS={
    DRAGON: ZOMBI,
    ZOMBI: VAMPIRO,
    VAMPIRO: DRAGON,
}

class Mostruo:
    def __init__(self):
        self.tipo = None

    def luchar(self, enemigo):
        if self.tipo == enemigo.tipo:
            return "igual"
        if REGLAS[self.tipo] == enemigo.tipo:
            return "fuerte"
        return "debil"


class Dragon(Mostruo):
    def __init__(self):
        self.tipo = DRAGON
    
    def __str__(self):
        return f"[{self.tipo}] 🐉 listo para luchar"
    
    
class Zombi(Mostruo):
    def __init__(self):
        self.tipo = ZOMBI
    def __str__(self):
        return f"[{self.tipo}] 🧟 listo para luchar"
    
    
class Vampiro(Mostruo):
    def __init__(self):
        self.tipo = VAMPIRO
    
    def __str__(self):
        return f"[{self.tipo}] 🧛 listo para luchar"


class Spawner:
    def crear(self):
        pass


class SpawnerDragon(Spawner):
    def crear(self):
        return Dragon()


class SpawnerZombi(Spawner):
    def crear(self):
        return Zombi()


class SpawnerVampiro(Spawner):
    def crear(self):
        return Vampiro()
    
class CreadorMostruos:
    def obtener_mostruo(self, tipo):
        if tipo == "dragon":
            return SpawnerDragon().crear()
        if tipo == "zombi":
            return SpawnerZombi().crear()
        if tipo == "vampiro":
            return SpawnerVampiro().crear()
        raise ValueError("❌ Mostruo no disponible. Intente de nuevo")
    

while True:
    print("\n\n🧩 Selección de Monstruos 🧩")
    print("Jugador 1: Elige tu monstruo (dragon/zombi/vampiro):")
    print("Jugador 2: Elige tu monstruo (dragon/zombi/vampiro):")
    print('Escribe "salir" para terminar.')
    jugador_uno = input("💬 Jugador 1, elige tu monstruo: ").lower().strip()
    jugador_dos = input("💬 Jugador 2, elige tu monstruo: ").lower().strip()
    if jugador_uno == "salir" or jugador_dos == "salir":
        print("\n🚶 Saliendo del juego.")
        break
    try:
        creador = CreadorMostruos()
        monstruo_uno = creador.obtener_mostruo(jugador_uno)
        print(monstruo_uno)
        monstruo_dos = creador.obtener_mostruo(jugador_dos)
        print(monstruo_dos)
        resultado = monstruo_uno.luchar(monstruo_dos)
        if resultado == "igual":
            print("🤝 Empate! Ambos monstruos son iguales.")
        if resultado == "fuerte":
            print("🏆 Jugador 1 gana! Su monstruo es más fuerte.")
        if resultado == "debil":
            print("🏆 Jugador 2 gana! Su monstruo es más fuerte.")
    except ValueError as e:
        print(e)