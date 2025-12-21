from .tarea import Tarea

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
            return

        for i, tarea in enumerate(self.tareas, 1):
            print(f"{i}. {tarea}")

    def completar_tarea(self, indice):
        if 0 < indice <= len(self.tareas):
            tarea = self.tareas[indice - 1]
            tarea.marcar_completada()
            print(f"Tarea '{tarea.descripcion}' marcada como completada.")
        else:
            print("Error: Índice de tarea inválido.")

    def eliminar_tarea(self, indice):
        if 0 < indice <= len(self.tareas):
            tarea_eliminada = self.tareas.pop(indice - 1)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada.")
        else:
            print("Error: Índice de tarea inválido.")

    def eliminar_tareas_completadas(self):
        self.tareas = [tarea for tarea in self.tareas if not tarea.estado_completada]
        print(f"Se han eliminado las tareas completadas.")

    def eliminar_todas_las_tareas(self):
        self.tareas.clear()
        print("Todas las tareas han sido eliminadas.")