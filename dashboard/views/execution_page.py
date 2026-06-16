import streamlit as st

from execution.task_manager import (
    TaskManager
)

from execution.action_tracker import (
    Tracker
)


tasks = (
    TaskManager()
)

tracker = (
    Tracker()
)


def render():

    st.title(
        "Execution"
    )

    items = (
        tasks.all()
    )

    st.metric(

        "Progress",

        tracker.status(
            items
        )
    )

    st.json(
        items
    )