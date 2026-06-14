import streamlit as st

from services.state import (
    memory
)


def render():

    st.title(
        "Memory"
    )

    items = (
        memory.load()
    )

    for item in reversed(
        items
    ):

        with st.expander(

            item.get(

                "goal",

                "Goal"
            )

        ):

            st.json(
                item
            )