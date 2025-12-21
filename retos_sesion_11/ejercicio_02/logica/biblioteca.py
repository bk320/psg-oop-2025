from modelos import Usuario

class Biblioteca:

    def __init__(self, catalogo):
        self.catalogo = catalogo
        self.prestamos = {}

    def mostrar_libros(self):
        print("\n--- CATÁLOGO DISPONIBLE ---")
        for i, libro in enumerate(self.catalogo, 1):
            print(f"{i}. {libro}")

    def registrar_prestamo(self, nombre_usuario, indice_libro):
        if 0 < indice_libro <= len(self.catalogo):
            libro = self.catalogo[indice_libro - 1]

            if nombre_usuario not in self.prestamos:
                self.prestamos[nombre_usuario] = Usuario(nombre_usuario)
            
            self.prestamos[nombre_usuario].libros_prestados.append(libro)
            print(f"Éxito: '{libro.titulo}' registrado para {nombre_usuario}.")
        else:
            print("Error: El número de libro no es válido.")

    def realizar_devolucion(self, nombre_usuario):
        if nombre_usuario in self.prestamos:
            self.prestamos.pop(nombre_usuario)
            print(f"Devolución: Se han liberado todos los libros de {nombre_usuario}.")
        else:
            print(f"El usuario {nombre_usuario} no tiene libros pendientes.")

    def mostrar_prestados(self):
        if not self.prestamos:
            print("\nNo hay préstamos activos.")
            return
        
        print("\n--- REGISTRO CENTRAL DE PRÉSTAMOS ---")
        for nombre, usuario in self.prestamos.items():
            titulos = ", ".join([l.titulo for l in usuario.libros_prestados])
            print(f"Usuario: {nombre} | Libros: [{titulos}]")