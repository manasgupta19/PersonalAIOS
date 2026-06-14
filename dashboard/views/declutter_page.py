import streamlit as st

from pathlib import Path

from services.state import (
    declutter
)


def render():

    st.title(
        "Declutter"
    )

    if st.button(
        "Scan Downloads"
    ):

        data = (

            declutter
            .scan(

                str(

                    Path.home()

                    /
                    "Downloads"
                )
            )
        )

        st.write(
            data
        )