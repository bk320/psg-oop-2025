class Calcular:
    """Clase para calcular funciones matemáticas.
    """
    def area(self, lado_uno: int, lado_dos: int) -> int:
        """Calcula el área de un rectángulo o cuadrado.

        Args:
            lado_uno (int): El primer lado del cuerpo geométrico.
            lado_dos (int): El segundo lado del cuerpo geométrico.

        Returns:
            int: El área calculada.
        """
        return lado_uno * lado_dos
area = Calcular()
print(area.area(5, 10)) # area de un rectángulo
print(area.area(5, 5)) # area de un cuadrado