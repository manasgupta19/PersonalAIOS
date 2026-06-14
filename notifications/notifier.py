from datetime import datetime


class NotificationEngine:

    def generate(
        self,
        history
    ):

        notes = []

        if not history:

            notes.append(
                "No goals tracked yet"
            )

            return notes

        recent = history[-5:]

        notes.append(
            f"Tracked goals: {len(history)}"
        )

        finance = 0
        career = 0
        brand = 0

        for item in recent:

            agents = item.get(
                "agents",
                []
            )

            if (
                "Finance Agent"
                in agents
            ):
                finance += 1

            if (
                "Career Agent"
                in agents
            ):
                career += 1

            if (
                "Personal Brand Agent"
                in agents
            ):
                brand += 1

        if career:
            notes.append(
                "Career momentum active"
            )

        if finance:
            notes.append(
                "Review financial actions"
            )

        if brand:
            notes.append(
                "Create one valuable social contribution"
            )

        notes.append(
            f"Updated: {datetime.now().strftime('%H:%M')}"
        )

        high = 0

        for item in recent:

            if (
                item.get(
                    "priority"
                )
                == "High"
            ):
                high += 1

        if high:

            notes.insert(
                0,
                f"{high} high priority items"
            )

        return notes