AGENTS = {

    "Career Agent": [
        "career",
        "job",
        "promotion",
        "interview"
    ],

    "Finance Agent": [
        "money",
        "finance",
        "investment",
        "salary"
    ],

    "Business Agent": [
        "business",
        "startup"
    ],

    "Decluttering Agent": [
        "declutter",
        "organize",
        "clean"
    ],

    "Personal Brand Agent": [
        "brand",
        "social",
        "content"
    ],

    "Digital Security Agent": [
        "privacy",
        "security",
        "password",
        "risk"
    ],

    "Research Agent": []
}


def select_agents(goal):

    goal = goal.lower()

    selected = []

    for name, keywords in AGENTS.items():

        if any(
            k in goal
            for k in keywords
        ):
            selected.append(name)

    if not selected:

        selected.append(
            "Research Agent"
        )

    return selected