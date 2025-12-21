class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.estado_completada = False

    def marcar_completada(self):
        self.estado_completada = True

    def __str__(self):
        estado = "✔️" if self.estado_completada else "❌"
        return f"[ {estado} ] {self.descripcion}"