class Digest:

    def create(
        self,
        notifications
    ):

        if not notifications:

            return [
                "No important updates"
            ]

        return [

            f"{len(notifications)} updates"

        ] + notifications