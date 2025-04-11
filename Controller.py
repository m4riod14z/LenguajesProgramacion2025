# La controladora no debe tener mensajes por pantalla
# Siempre tiene las funciones de entrada

from Model import TaskModel
from View import TaskView

class TaskController:

    def __init__(this, model: TaskModel, view: TaskView):
        this.model = model
        this.view = view

    def addTask(this):
        # Captura información de la vista:
        newTask = this._view.promptForAdd()
        # Actualiza el modelo con lo que la vista devuelve:
        this._model.addTask(newTask)
        this._view.showMessage("La tarea ha sido agregada")

    # Completar:
    def removeTask(this):
        pass

    # Completar:
    def showTasks(this):
        pass

    # Menú del controlador:
    def runController(this):
        pass