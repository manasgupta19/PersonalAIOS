class OpportunityEngine:

    def generate(
        self,
        profile,
        history
    ):

        ideas = []

        focus = (
            profile
            .get(
                "focus",
                ""
            )
            .lower()
        )

        values = (
            profile
            .get(
                "values",
                ""
            )
            .lower()
        )

        if (
            "career"
            in focus
        ):

            ideas.append({

                "title":
                    "Career Leverage",

                "action":
                    "Define one skill that compounds over 3 years"
            })

        if (
            "growth"
            in values
        ):

            ideas.append({

                "title":
                    "Public Learning",

                "action":
                    "Share one useful insight this week"
            })

        if len(
            history
        ) > 3:

            ideas.append({

                "title":
                    "Declutter Momentum",

                "action":
                    "Review active goals and archive stale ones"
            })

        if not ideas:

            ideas.append({

                "title":
                    "Explore",

                "action":
                    "Define one meaningful objective"
            })

        brand_count = 0

        for h in history:

            if (
                "Personal Brand Agent"
                in h.get(
                    "agents",
                    []
                )
            ):

                brand_count += 1

        if brand_count:

            ideas.append({

                "title":
                    "Personal Brand",

                "action":
                    "Publish one insight that genuinely helps people"
            })
        return ideas