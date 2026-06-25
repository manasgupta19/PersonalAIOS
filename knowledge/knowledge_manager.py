import os

from storage.json_store import (
    JsonStore
)


class KnowledgeManager:

    def __init__(self):

        self.path = (
            "knowledge/knowledge.json"
        )

        self.store = (
            JsonStore()
        )


    def save(
        self,
        item,
        kind
    ):

        self.store.append(

            self.path,

            {
                "type": kind,
                "value": item
            }

        )


    def load(self):

        return self.store.load(
            self.path
        )