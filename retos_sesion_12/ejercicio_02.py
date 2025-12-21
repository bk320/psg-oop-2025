class Tarea:
    """
    Representa una tarea individual en el sistema.

    Attributes
    ----------
    titulo : str
        El título breve de la tarea.
    descripcion : str
        La explicación detallada de la tarea.
    esta_completada : bool
        Estado de la tarea (True si está hecha, False de lo contrario).
    """

    def __init__(self, titulo: str, descripcion: str) -> None:
        """
        Inicializa una nueva tarea.
        """
        self.titulo: str = titulo
        self.descripcion: str = descripcion
        self.esta_completada: bool = False

    def marcar_completada(self) -> None:
        """
        Cambia el estado de la tarea a completada.
        """
        self.esta_completada = True


class GestorDeTareas:
    """
    Administra una coleccion de tareas para la empresa de citas.

    Attributes
    ----------
    tareas : list[Tarea]
        Lista que almacena los objetos de tipo Tarea.
    """

    def __init__(self) -> None:
        """
        Inicializa el gestor con una lista vacia.
        """
        self.tareas: list[Tarea] = []

    def agregar_tarea(self, titulo: str, descripcion: str) -> None:
        """
        Crea y añade una nueva tarea a la lista.

        Parameters
        ----------
        titulo : str
            Título de la tarea.
        descripcion : str
            Descripción de la tarea.
        """
        nueva_tarea = Tarea(titulo, descripcion)
        self.tareas.append(nueva_tarea)
        print(f"✅ Tarea '{titulo}' agregada con éxito.")

    def _buscar_tarea(self, titulo: str) -> Tarea | None:
        """
        Método privado para buscar una tarea por título (Principio DRY).

        Parameters
        ----------
        titulo : str
            El titulo de la tarea a buscar.

        Returns
        -------
        Tarea | None
            El objeto Tarea si se encuentra, de lo contrario None.
        """
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                return tarea
        return None

    def eliminar_tarea(self, titulo: str) -> None:
        """
        Busca y elimina una tarea de la lista por su titulo.

        Parameters
        ----------
        titulo : str
            El titulo de la tarea a eliminar.
        """
        tarea = self._buscar_tarea(titulo)
        if tarea:
            self.tareas.remove(tarea)
            print(f"🗑️ Tarea '{titulo}' eliminada.")
        else:
            print(f"⚠️ No se encontró la tarea con titulo '{titulo}'.")

    def marcar_tarea_completada(self, titulo: str) -> None:
        """
        Busca una tarea y la marca como completada.

        Parameters
        ----------
        titulo : str
            El titulo de la tarea a completar.
        """
        tarea = self._buscar_tarea(titulo)
        if tarea:
            tarea.marcar_completada()
            print(f"✔️ Tarea '{titulo}' marcada como completada.")
        else:
            print(f"⚠️ No se encontro la tarea con titulo '{titulo}'.")

    def listar_tareas(self) -> None:
        """
        Muestra en pantalla todas las tareas registradas y su estado.
        """
        if not self.tareas:
            print("\n📭 La lista de tareas está vacía.")
            return

        print("\n--- Lista de Tareas ---")
        for tarea in self.tareas:
            estado = "✅ Completada" if tarea.esta_completada else "⏳ Pendiente"
            print(f"[{estado}] {tarea.titulo}: {tarea.descripcion}")


def menu():
    """
    Función principal que gestiona el menú interactivo del programa.
    """
    gestor = GestorDeTareas()

    while True:
        print("\n--- MENU GESTOR DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Marcar tarea como completada")
        print("4. Listar tareas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            t = input("Título: ")
            d = input("Descripción: ")
            gestor.agregar_tarea(t, d)
        elif opcion == "2":
            t = input("Título de la tarea a eliminar: ")
            gestor.eliminar_tarea(t)
        elif opcion == "3":
            t = input("Título de la tarea a completar: ")
            gestor.marcar_tarea_completada(t)
        elif opcion == "4":
            gestor.listar_tareas()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("⚠️ Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()