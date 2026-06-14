import streamlit as st

from services.state import (
    knowledge
)


def render():

    st.title(
        "Knowledge"
    )

    q = st.text_input(
        "Search"
    )

    if q:

        result = (

            knowledge
            .search(
                q
            )
        )

        st.json(
            result
        )