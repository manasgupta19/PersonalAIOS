import streamlit as st


def render(
    actions
):

    st.subheader(
        "Agent Output"
    )

    for name, items in actions.items():

        with st.expander(
            name
        ):

            for i in items:

                st.write(
                    i
                )