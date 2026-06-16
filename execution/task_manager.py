import json
from pathlib import Path


FILE = (
    Path(__file__)
    .parent
    /
    "tasks.json"
)


class TaskManager:

    def load(self):

        if not FILE.exists():

            return []

        text = FILE.read_text()

        if not text.strip():

            return []

        return json.loads(text)

    def save(
        self,
        task
    ):

        data = (
            self.load()
        )

        data.append(
            task
        )

        FILE.write_text(

            json.dumps(
                data,
                indent=2
            )
        )

    def all(self):

        return self.load()