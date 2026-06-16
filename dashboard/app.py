import bootstrap
import streamlit as st

from views.dashboard_page import render as dashboard
from views.memory_page import render as memory
from views.knowledge_page import render as knowledge
from views.notifications_page import render as notifications
from views.opportunities_page import render as opportunities
from views.declutter_page import render as declutter
from views.settings_page import render as settings
from views.execution_page import render as execution
from views.planning_page import render as planning


PAGES = {
    "Dashboard": dashboard,
    "Memory": memory,
    "Knowledge": knowledge,
    "Notifications": notifications,
    "Opportunities": opportunities,
    "Declutter": declutter,
    "Settings": settings,
    "Execution": execution,
    "Planning": planning,
}


st.set_page_config(
    page_title="Personal AI OS",
    page_icon="🧠",
    layout="wide",
)


with st.sidebar:

    st.title("Personal AI OS")

    page = st.selectbox(
        "Navigate",
        list(PAGES.keys())
    )

    st.divider()

    st.caption("v0.1")


PAGES[page]()