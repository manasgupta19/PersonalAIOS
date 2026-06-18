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

from execution.executor import (
    create_plan
)

from automation.scheduler import (
    Scheduler
)

brief = (
    Scheduler()
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

        st.subheader(
            "Chief Of Staff"
        )

        st.write(
            data[
                "insight"
            ]
        )

    plan = (
        create_plan(
            goal
        )
    )

    st.subheader(
        "Execution Plan"
    )

    st.json(
        plan
    )

    st.info(

        f"""
    Daily Briefing

    {brief.morning_briefing()['time']}
    """
    )