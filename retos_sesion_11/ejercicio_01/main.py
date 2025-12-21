from models import ListaTareas

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Eliminar tareas completadas")
    print("6. Eliminar todas las tareas")
    print("7. Salir")

def ejecutar_programa():
    lista = ListaTareas()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            desc = input("Ingrese la descripción de la tarea: ")
            lista.agregar_tarea(desc)
        elif opcion == "2":
            lista.mostrar_tareas()
        elif opcion == "3":
            lista.mostrar_tareas()
            try:
                indice_tarea_completar = int(input("Índice de la tarea a completar: "))
                lista.completar_tarea(indice_tarea_completar)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == "4":
            lista.mostrar_tareas()
            try:
                indice_tarea_eliminar = int(input("Índice de la tarea a eliminar: "))
                lista.eliminar_tarea(indice_tarea_eliminar)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == "5":
            lista.eliminar_tareas_completadas()
        elif opcion == "6":
            lista.eliminar_todas_las_tareas()
        elif opcion == "7":
            print("¡Gracias por usar la aplicación! 👋")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    ejecutar_programa()