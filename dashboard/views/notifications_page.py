import streamlit as st

from services.state import (

    notify,

    memory
)


def render():

    st.title(
        "Notifications"
    )

    notes = (

        notify.generate(

            memory.load()
        )
    )

    for n in notes:

        st.info(
            n
        )