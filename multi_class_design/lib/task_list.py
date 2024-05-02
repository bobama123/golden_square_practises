class TaskList:
    # User-facing properties:
    #   task: list of instances of Task

    def __init__(self):
        self.task_list = []

    def add(self, task):
        self.task_list.append(task)

    def list_incomplete(self):
        return self.task_list

    def list_complete(self):
        complete_list = []
        for task in self.task_list:
            if task.complete == True:
                complete_list.append(task)
        return complete_list
        