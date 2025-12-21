from modelos import Libro
from logica import Biblioteca

def mostrar_menu():
    print("\n--- SISTEMA BIBLIOTECARIO ---")
    print("1. Realizar préstamo")
    print("2. Ver lista de préstamos")
    print("3. Devolver todos los libros")
    print("Escriba 'salir' para finalizar.")

def main():
    catalogo = [
        Libro("Cien años de soledad", "Gabriel García Márquez", "978-01"),
        Libro("1984", "George Orwell", "978-02"),
        Libro("El Principito", "A. de Saint-Exupéry", "978-03"),
        Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-04"),
        Libro("La Odisea", "Homero", "978-05")
    ]
    biblioteca = Biblioteca(catalogo)

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip().lower()

        if opcion == "salir":
            print("Cerrando sistema... 👋")
            break
        
        if opcion == "1":
            nombre = input("Ingrese su nombre: ").lower().strip()
            biblioteca.mostrar_libros()
            try:
                idx = int(input("Seleccione el número del libro: "))
                biblioteca.registrar_prestamo(nombre, idx)
            except ValueError:
                print("Error: Ingrese un número válido.")

        elif opcion == "2":
            biblioteca.mostrar_prestados()

        elif opcion == "3":
            nombre = input("Nombre del usuario que devuelve: ")
            biblioteca.realizar_devolucion(nombre)
        
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()