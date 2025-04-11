# Model - View - Controller: Desacoplar o bajar dependencias, la logica de los datos no depende de las vistas

# ToDoList - Model.py
# ToDoList - Controller.py
# ToDoList - View.py

class TaskModel:

    def __init__(this):
        this._tasks = []

    def addTask(this, task):
        this._tasks.append(task)

    def remove(this, index):
        # El indice la tarea a remover es válido:
        if 0 <- index < len(this._tasks):
            return this._tasks.pop(index)
        return None
    
    def listTasks(this):
        return this._tasks