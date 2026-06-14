from agents.modules.career import CareerAgent
from agents.modules.finance import FinanceAgent
from agents.modules.declutter import DeclutteringAgent
from agents.modules.brand import PersonalBrandAgent
from agents.modules.research import ResearchAgent


MAP = {

    "Career Agent":
        CareerAgent(),

    "Finance Agent":
        FinanceAgent(),

    "Decluttering Agent":
        DeclutteringAgent(),

    "Personal Brand Agent":
        PersonalBrandAgent(),

    "Research Agent":
        ResearchAgent()
}


def execute_agents(
    goal,
    selected
):

    result = {}

    for a in selected:

        if a in MAP:

            result[a] = (
                MAP[a]
                .execute(goal)
            )

    return result