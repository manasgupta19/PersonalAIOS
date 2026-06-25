from storage.json_store import (
    JsonStore
)


class MemoryManager:

    def __init__(self):

        self.path = (
            "memory/goals.json"
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
        goals
    ):

        self.store.save(
            self.path,
            goals
        )


    def add(
        self,
        goal
    ):

        self.store.append(
            self.path,
            goal
        )