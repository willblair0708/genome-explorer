"""Main Streamlit application for Genome Explorer AI."""

import streamlit as st
from typing import Literal

from genome_explorer.core.config import AppConfig
from genome_explorer.core.session import init_session_state
from genome_explorer.visualization.pages import genome_viewer
from genome_explorer.ai.pages import ai_assistant
from genome_explorer.simulation.pages import simulation_lab
from genome_explorer.reports.pages import genome_reports
from genome_explorer.education.pages import learning_hub

# App configuration
st.set_page_config(
    page_title="Genome Explorer AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
init_session_state()

# Sidebar navigation
def render_sidebar() -> Literal["Visualizer", "AI Assistant", "Simulation Lab", "Reports", "Learning"]:
    """Render sidebar navigation and return selected page."""
    st.sidebar.title("🧬 Genome Explorer AI")
    
    return st.sidebar.radio(
        "Navigation",
        options=["Visualizer", "AI Assistant", "Simulation Lab", "Reports", "Learning"],
        index=0,
    )

def main():
    """Main application entry point."""
    # Navigation
    page = render_sidebar()
    
    # Page routing
    if page == "Visualizer":
        genome_viewer.render()
    elif page == "AI Assistant":
        ai_assistant.render()
    elif page == "Simulation Lab":
        simulation_lab.render()
    elif page == "Reports":
        genome_reports.render()
    else:
        learning_hub.render()

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        "Made with ❤️ by [William Blair](https://github.com/willblair0708)"
    )

if __name__ == "__main__":
    main() 