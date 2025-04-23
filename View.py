# Logica que permite mostrar lo que está en el modelo

class TaskView:

    def showAllTasks(this, tasks):
        print("\nLista de tareas:")
        if not tasks:
            print("No hay tareas pendientes")
        else:
            for i, t in enumerate(tasks):
                print(f"Tarea {i+1} - {t}")

    def promptForAdd(this):
        description = input("Ingrese una nueva tarea:")
        priority = input("Ingrese la prioridad (baja, media, alta): ").lower()
        return description, priority

    def promptForRemove(this):
        return int(input("Ingrese el indice de la tarea a eliminar"))
    
    def promptForPriority(this):
        return input("¿Qué prioridad desea mostrar? (baja, media, alta): ").lower()
    
    def menu(this):
        print("\n1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar todas las tareas")
        print("4. Mostrar tareas por prioridad")
        print("5. Salir")
        return int(input("Seleccione una opción: "))

    def showMessage(this, msg):
        print(msg)