from storage.json_store import (
    JsonStore
)


class TaskManager:

    def __init__(self):

        self.path = (
            "execution/tasks.json"
        )

        self.store = (
            JsonStore()
        )


    def load(self):

        return self.store.load(
            self.path,
            []
        )


    def save(
        self,
        tasks
    ):

        self.store.save(
            self.path,
            tasks
        )


    def add(
        self,
        task
    ):

        self.store.append(
            self.path,
            task
        )