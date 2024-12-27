"""Session state management for Streamlit application."""

from typing import Any, Dict, Optional
import streamlit as st

def init_session_state() -> None:
    """Initialize session state with default values."""
    
    # User preferences
    if "theme" not in st.session_state:
        st.session_state.theme = "light"
    
    # Genome data
    if "current_genome" not in st.session_state:
        st.session_state.current_genome = None
    if "genome_history" not in st.session_state:
        st.session_state.genome_history = []
    
    # AI/ML state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "model_cache" not in st.session_state:
        st.session_state.model_cache = {}
    
    # Simulation state
    if "simulation_params" not in st.session_state:
        st.session_state.simulation_params = {
            "mutation_rate": 0.001,
            "population_size": 100,
            "generations": 10,
        }
    
    # Education progress
    if "completed_modules" not in st.session_state:
        st.session_state.completed_modules = set()
    if "quiz_scores" not in st.session_state:
        st.session_state.quiz_scores = {}

def get_state(key: str, default: Any = None) -> Any:
    """Get value from session state with default."""
    return st.session_state.get(key, default)

def set_state(key: str, value: Any) -> None:
    """Set value in session state."""
    st.session_state[key] = value

def update_state(updates: Dict[str, Any]) -> None:
    """Batch update multiple session state values."""
    for key, value in updates.items():
        set_state(key, value)

def clear_state(keys: Optional[list[str]] = None) -> None:
    """Clear specified keys or entire session state."""
    if keys is None:
        # Clear all except theme
        theme = get_state("theme")
        st.session_state.clear()
        set_state("theme", theme)
    else:
        for key in keys:
            if key in st.session_state:
                del st.session_state[key] 