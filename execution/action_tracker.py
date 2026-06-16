class Tracker:

    def status(
        self,
        tasks
    ):

        total = len(tasks)

        done = len(

            [

                t

                for t

                in tasks

                if t.get(
                    "done"
                )
            ]

        )

        if total == 0:

            return 0

        return int(

            done
            /
            total

            *
            100
        )