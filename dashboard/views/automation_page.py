import streamlit as st

from automation.event_loop import (
    run
)


def render():

    st.title(
        "Automation"
    )

    if st.button(
        "Generate Suggestions"
    ):

        actions = run()

        if not actions:

            st.success(
                "No suggestions."
            )

            return

        for idx, a in enumerate(actions):

            action = a.get(
                "action",
                "Unnamed action"
            )

            approved = a.get(
                "approved",
                False
            )

            with st.container():

                col1, col2 = st.columns(
                    [5, 1]
                )

                with col1:

                    st.write(
                        action
                    )

                with col2:

                    clicked = st.button(

                        "Approve",

                        key=f"approve_{idx}"

                    )

                    if clicked:

                        a[
                            "approved"
                        ] = True

                        st.success(
                            f"Approved #{idx+1}"
                        )

                if approved:

                    st.caption(
                        "Approved"
                    )