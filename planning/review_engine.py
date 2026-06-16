class Review:

    def summarize(
        self,
        tasks
    ):

        total = len(
            tasks
        )

        done = len([

            t

            for t

            in tasks

            if t.get(
                "done"
            )

        ])

        return {

            "total":
                total,

            "done":
                done,

            "remaining":
                total
                -
                done
        }