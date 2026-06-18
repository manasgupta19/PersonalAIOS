import streamlit as st

from execution.task_manager import (
    TaskManager
)

from notifications.notifier import (
    NotificationEngine
)


tasks = (
    TaskManager()
)

notify = (
    NotificationEngine()
)


def render():

    st.title(
        "Notifications"
    )

    alerts = (

        notify
        .generate(

            tasks.all()

        )
    )

    for a in alerts:

        st.info(
            a
        )