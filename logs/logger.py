from pathlib import Path
from datetime import datetime


LOG = (
    Path(__file__)
    .parent
    / "events.log"
)


def write(
    event
):

    with open(
        LOG,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(

            f"{datetime.now()} "

            f"{event}\n"
        )