class TaskTracker():
    def __init__(self):
        self._tasks = []

    def add (self, task):
        self._tasks.append(task)
        # Parameters:
        #   Task : string representing a tasks

    def list_incomplete(self):
        return self._tasks
        # Returns:
        #   A list of incomplete tasks

    def mark_complete(self, index):
        if index < 0 or index >= len(self._tasks):
            raise Exception("No such task to mark complete")
        del self._tasks[index]
        # Parameters:
        #   index: on integer representing the task to complete
        # Side-effect:
        #   Removes the task at index from list of tasks
