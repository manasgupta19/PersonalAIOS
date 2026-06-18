from datetime import (
    datetime
)


class Scheduler:

    def morning_briefing(self):

        return {

            "time":
                datetime.now()
                .isoformat(),

            "enabled":
                True
        }