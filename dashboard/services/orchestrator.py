from agents.chief_of_staff import (
    ChiefOfStaff
)

from agents.executor import (
    execute_agents
)

from collaboration.council import (
    AgentCouncil
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

    return {

        "result":
            result,

        "actions":
            actions,

        "coordination":
            coordination
    }