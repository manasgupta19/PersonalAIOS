import streamlit as st

from services.state import (

    opportunity,

    profile,

    memory
)


def render():

    st.title(
        "Opportunities"
    )

    items = (

        opportunity
        .generate(

            profile.load(),

            memory.load()
        )
    )

    for i in items:

        with st.expander(

            i[
                "title"
            ]

        ):

            st.write(

                i[
                    "action"
                ]
            )