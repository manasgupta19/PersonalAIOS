import streamlit as st


def render(
    settings,
    memory,
    knowledge
):

    st.metric(

        "Version",

        settings[
            "version"
        ]
    )

    st.metric(

        "Goals",

        len(
            memory.load()
        )
    )

    st.metric(

        "Knowledge",

        len(
            knowledge.load()
        )
    )