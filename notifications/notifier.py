from notifications.rules import (
    NotificationRules
)

from notifications.digest import (
    Digest
)


class NotificationEngine:

    def __init__(self):

        self.rules = (
            NotificationRules()
        )

        self.digest = (
            Digest()
        )

    def generate(
        self,
        tasks
    ):

        alerts = (

            self.rules
            .evaluate(
                tasks
            )
        )

        return (

            self.digest
            .create(
                alerts
            )
        )