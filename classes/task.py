from classes.subtask import Subtask


class Task:
    def __init__(self, name, dueDate="", taskID=0, description="", workload=0, priority=0, subtasks:list[str]=None, completed=False):
        self._taskID = taskID  # Use a different name for the attribute
        self._name = name
        self._dueDate = dueDate
        self._description = description
        self._workload = workload
        self._priority = priority
        self._subtasks = []
        if subtasks is not None:
            for subtask in subtasks:
                self._subtasks.append(Subtask(id=subtasks.index(subtask), name=subtask, parent=self))
        self._completed = completed

    # Getters
    @property
    def taskID(self): return self._taskID
    @property
    def name(self): return self._name
    @property
    def description(self): return self._description
    @property
    def workload(self): return self._workload
    @property
    def priority(self): return self._priority
    @property
    def subtasks(self): return self._subtasks
    @property
    def dueDate(self): return self._dueDate
    @property
    def completed(self): return self._completed

    # Setters
    @name.setter
    def name(self, newName): self._name = newName
    @description.setter
    def description(self, newDesc): self._description = newDesc
    @priority.setter
    def priority(self, newPrio): self._priority = newPrio
    @taskID.setter
    def taskID(self, newID): self._taskID = newID
    @dueDate.setter
    def dueDate(self, newDue): self._dueDate = newDue

    def addSubtask(self, newSub: Subtask):
        self._subtasks.append(newSub)

    def markComplete(self): self._completed = True