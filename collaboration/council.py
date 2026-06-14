class AgentCouncil:

    def collaborate(
        self,
        goal,
        actions
    ):

        result = []

        names = list(
            actions.keys()
        )

        if (
            "Career Agent"
            in names
            and
            "Personal Brand Agent"
            in names
        ):

            result.append(
                (
                    "Career ↔ Brand",
                    (
                        "Convert one professional "
                        "insight into a public post"
                    )
                )
            )

        if (
            "Career Agent"
            in names
            and
            "Finance Agent"
            in names
        ):

            result.append(
                (
                    "Career ↔ Finance",
                    (
                        "Prioritize skills with "
                        "long-term earning leverage"
                    )
                )
            )

        if (
            "Decluttering Agent"
            in names
        ):

            result.append(
                (
                    "Declutter",
                    (
                        "Reduce active commitments "
                        "before adding new goals"
                    )
                )
            )

        if not result:

            result.append(
                (
                    "Research",
                    (
                        "Gather more information "
                        "before coordination"
                    )
                )
            )

        return result