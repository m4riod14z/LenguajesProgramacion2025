# La controladora no debe tener mensajes por pantalla
# Siempre tiene las funciones de entrada

from Model import TaskModel
from View import TaskView
from TaskFactory import LowPriorityFactory, MediumPriorityFactory, HighPriorityFactory

class TaskController:

    def __init__(this, model: TaskModel, view: TaskView):
        this._model = model
        this._view = view

    def addTask(this):
        description, priority = this._view.promptForAdd()
        factory = this._getFactory(priority)
        if factory:
            task = factory.create_task(description)
            this._model.addTask(task)
            this._view.showMessage("La tarea ha sido agregada")
        else:
            this._view.showMessage("Prioridad no válida")

    def removeTask(this):
        index = this._view.promptForRemove() - 1
        removed = this._model.remove(index)
        if removed:
            this._view.showMessage(f"Tarea '{removed}' eliminada")
        else:
            this._view.showMessage("Índice inválido")

    def showTasks(this):
        tasks = this._model.listTasks()
        this._view.showAllTasks(tasks)

    def showTasksByPriority(this, priority):
        tasks = this._model.listTasksByPriority(priority)
        this._view.showAllTasks(tasks)

    def runController(this):
        while True:
            option = this._view.menu()
            if option == 1:
                this.addTask()
            elif option == 2:
                this.removeTask()
            elif option == 3:
                this.showTasks()
            elif option == 4:
                priority = this._view.promptForPriority()
                this.showTasksByPriority(priority)
            elif option == 5:
                break
            else:
                this._view.showMessage("Opción inválida")

    def _getFactory(this, priority):
        if priority == "baja":
            return LowPriorityFactory()
        elif priority == "media":
            return MediumPriorityFactory()
        elif priority == "alta":
            return HighPriorityFactory()
        else:
            return None