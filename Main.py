from Model import TaskModel
from Controller import TaskController
from View import TaskView

if __name__ == "__main__":
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model=model, view=view)
    controller.runController()

# Modificar para que se tengan 3 tipos de tareas (Usando patrones de diseño)
# Tareas: Prioridad baja, prioridad media, prioridad alta

# Mostrar tareas con alta prioridad
# Mostrar tareas con baja prioridad

# Sugerir una mejora a la lista de tareas con un patron de diseño