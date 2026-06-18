import streamlit as st

from pathlib import Path

from declutter.scanner import (
    DeclutterScanner
)


scanner = (
    DeclutterScanner()
)


def render():

    st.title(
        "Declutter"
    )

    folder = st.text_input(

        "Folder",

        str(
            Path.home()
            /
            "Downloads"
        )
    )

    if st.button(
        "Analyze"
    ):

        result = (

            scanner.scan(
                folder
            )
        )

        st.subheader(
            "Review"
        )

        st.json(
            result
        )