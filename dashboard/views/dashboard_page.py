import streamlit as st

from services.orchestrator import (
    analyze
)

from services.state import (

    memory,

    knowledge
)

from components.goal_input import (
    render as input_box
)

from components.agent_output import (
    render as agent_output
)

from components.council_output import (
    render as council_output
)


def render():

    st.title(
        "Dashboard"
    )

    goal = (
        input_box()
    )

    if st.button(
        "Analyze"
    ):

        data = (
            analyze(
                goal
            )
        )

        memory.save_goal(
            data[
                "result"
            ]
        )

        knowledge.save(
            goal,
            "goal"
        )

        st.success(
            "Processed"
        )

        st.json(
            data[
                "result"
            ]
        )

        agent_output(
            data[
                "actions"
            ]
        )

        council_output(
            data[
                "coordination"
            ]
        )