class Task:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description

class LowPriorityTask(Task):
    def __str__(self):
        return f"[Baja] {self.description}"

class MediumPriorityTask(Task):
    def __str__(self):
        return f"[Media] {self.description}"

class HighPriorityTask(Task):
    def __str__(self):
        return f"[Alta] {self.description}"

class AbstractTaskFactory:
    def create_task(self, description):
        pass

class LowPriorityFactory(AbstractTaskFactory):
    def create_task(self, description):
        return LowPriorityTask(description)

class MediumPriorityFactory(AbstractTaskFactory):
    def create_task(self, description):
        return MediumPriorityTask(description)

class HighPriorityFactory(AbstractTaskFactory):
    def create_task(self, description):
        return HighPriorityTask(description)