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
        return input("Ingrese una nueva tarea:")

    def promptForRemove(this):
        return int(input("Ingrese el indice de la tarea a eliminar"))
    
    def showMessage(msg):
        print(msg)