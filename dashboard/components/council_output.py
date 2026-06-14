import streamlit as st


def render(
    coordination
):

    st.subheader(
        "Agent Council"
    )

    for team, advice in coordination:

        st.info(
            team
        )

        st.write(
            advice
        )