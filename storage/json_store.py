import json
from pathlib import Path


class JsonStore:

    def load(
        self,
        path,
        default=None
    ):

        file = Path(path)

        if not file.exists():

            return (
                default
                if default is not None
                else []
            )

        try:

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                return json.load(
                    f
                )

        except Exception:

            return (
                default
                if default is not None
                else []
            )


    def save(
        self,
        path,
        data
    ):

        Path(
            path
        ).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=2
            )


    def append(
        self,
        path,
        item
    ):

        data = self.load(
            path,
            []
        )

        if not isinstance(
            data,
            list
        ):

            data = []

        data.append(
            item
        )

        self.save(
            path,
            data
        )