from datetime import (
    datetime,
    timedelta
)


class Timeline:

    def generate(
        self,
        goal
    ):

        now = datetime.now()

        return [

            {

                "task":
                    goal,

                "due":

                    (
                        now
                        +
                        timedelta(
                            days=7
                        )
                    ).isoformat()

            }

        ]