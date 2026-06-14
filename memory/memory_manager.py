import json
from pathlib import Path


MEMORY_FILE = (
    Path(__file__)
    .parent
    / "goals.json"
)


class MemoryManager:

    def __init__(self):

        if not MEMORY_FILE.exists():

            MEMORY_FILE.write_text(
                "[]",
                encoding="utf-8"
            )

    def load(self):

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    def save_goal(self, data):

        memory = self.load()

        memory.append(data)

        with open(
            MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                memory,
                f,
                indent=2
            )