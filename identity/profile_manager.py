import json
from pathlib import Path


PROFILE = (
    Path(__file__)
    .parent
    / "profile.json"
)


class ProfileManager:

    def load(self):

        try:

            with open(
                PROFILE,
                "r",
                encoding="utf-8"
            ) as f:

                return json.load(f)

        except:

            return {}

    def save(
        self,
        data
    ):

        with open(
            PROFILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=2
            )