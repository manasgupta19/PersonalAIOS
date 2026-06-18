class NotificationRules:

    def evaluate(
        self,
        tasks
    ):

        alerts = []

        for t in tasks:

            due = str(
                t.get(
                    "due",
                    ""
                )
            )

            if not t.get(
                "done",
                False
            ):

                alerts.append(

                    f"Pending: {t['task']}"

                )

        return alerts