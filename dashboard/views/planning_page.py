import streamlit as st

from execution.task_manager import (
    TaskManager
)

from planning.priority_engine import (
    PriorityEngine
)

from planning.scheduler import (
    Scheduler
)

from planning.review_engine import (
    Review
)


tasks = (
    TaskManager()
)

priority = (
    PriorityEngine()
)

schedule = (
    Scheduler()
)

review = (
    Review()
)


def render():

    st.title(
        "Planning"
    )

    data = (
        tasks.all()
    )

    ranked = (
        priority.rank(
            data
        )
    )

    plan = (
        schedule.schedule(
            ranked
        )
    )

    st.metric(

        "Remaining",

        review
        .summarize(
            data
        )[
            "remaining"
        ]
    )

    st.subheader(
        "Today"
    )

    st.json(
        plan[
            "today"
        ]
    )

    st.subheader(
        "This Week"
    )

    st.json(
        plan[
            "week"
        ]
    )

    st.subheader(
        "Later"
    )

    st.json(
        plan[
            "later"
        ]
    )