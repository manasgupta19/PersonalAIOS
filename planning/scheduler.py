from datetime import (
    datetime
)


class Scheduler:

    def schedule(
        self,
        tasks
    ):

        plan = {

            "today": [],

            "week": [],

            "later": []
        }

        for t in tasks:

            due = datetime.fromisoformat(
                t["due"]
            )

            days = (

                due
                -
                datetime.now()

            ).days

            if days <= 1:

                plan[
                    "today"
                ].append(
                    t
                )

            elif days <= 7:

                plan[
                    "week"
                ].append(
                    t
                )

            else:

                plan[
                    "later"
                ].append(
                    t
                )

        return plan