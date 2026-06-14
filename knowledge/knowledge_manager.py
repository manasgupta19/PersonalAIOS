import json
from pathlib import Path


FILE = (
    Path(__file__)
    .parent
    / "knowledge.json"
)


class KnowledgeManager:

    def __init__(self):

        if not FILE.exists():

            FILE.write_text(
                "[]",
                encoding="utf-8"
            )

    def load(self):

        try:

            with open(
                FILE,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

                if not isinstance(
                    data,
                    list
                ):

                    return []

                return data

        except:

            return []

    def save(
        self,
        text,
        source
    ):

        if not text:

            return

        data = self.load()

        entry = {

            "text":
                str(text),

            "source":
                source
        }

        if entry not in data:

            data.append(
                entry
            )

        with open(
            FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=2
            )

    def search(
        self,
        query
    ):

        if not query:

            return []

        q = query.lower()

        result = []

        for item in self.load():

            if (

                q
                in
                item["text"]
                .lower()

            ):

                result.append(
                    item
                )

        return result[:10]