import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# -------------------------------------------------------
# Streamlit Page Configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="Global Two-Phase Immersion Cooling Market | GRC Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------------
# Hide Streamlit Default UI Elements
# -------------------------------------------------------
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }

        iframe {
            width: 100%;
            min-height: 100vh;
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------
# Load HTML Dashboard
# -------------------------------------------------------
html_file = Path("dashboard.html")

if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")

    components.html(
        html_content,
        height=9000,
        scrolling=True
    )
else:
    st.error(
        "dashboard.html file not found. Please save your full HTML page as dashboard.html "
        "in the same folder as app.py."
    )