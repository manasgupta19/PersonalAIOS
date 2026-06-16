from agents.chief_of_staff import (
    ChiefOfStaff
)

from agents.executor import (
    execute_agents
)

from collaboration.council import (
    AgentCouncil
)

from llm.client import (
    Brain
)

brain = (
    Brain()
)


cos = (
    ChiefOfStaff()
)

council = (
    AgentCouncil()
)


def analyze(
    goal
):

    result = (
        cos.analyze(
            goal
        )
    )

    actions = (

        execute_agents(

            goal,

            result[
                "agents"
            ]
        )
    )

    coordination = (

        council
        .collaborate(

            goal,

            actions
        )
    )

    insight = (

        brain.ask(

            f"""

    Goal:

    {goal}

    Provide:

    1 analysis

    2 risks

    3 actions

    4 opportunities
    """
        )
    )

    return {

        "result":
            result,

        "actions":
            actions,

        "coordination":
            coordination,

        "insight":
            insight
    }