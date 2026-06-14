import streamlit as st

from configs.settings import (
    SETTINGS
)


def render():

    st.title(
        "Settings"
    )

    st.json(
        SETTINGS
    )