from agents.registry import (
    select_agents
)


class ChiefOfStaff:

    def analyze(
        self,
        goal
    ):

        agents = (
            select_agents(goal)
        )

        return {

            "goal": goal,

            "priority":
                self.priority(goal),

            "agents":
                agents
        }

    def priority(
        self,
        goal
    ):

        goal = goal.lower()

        urgent = [

            "urgent",
            "deadline",
            "today",
            "critical"
        ]

        if any(
            x in goal
            for x in urgent
        ):

            return "High"

        return "Medium"