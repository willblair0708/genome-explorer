"""AI-powered genomics assistant page."""

import streamlit as st
from typing import List, Tuple

from genome_explorer.core import get_state, set_state

def render_chat_message(
    message: Tuple[str, str, str]
) -> None:
    """Render a chat message."""
    role, content, timestamp = message
    
    if role == "user":
        st.markdown(f"**You** ({timestamp})")
        st.markdown(content)
    else:
        st.markdown(f"**🧬 Genome AI** ({timestamp})")
        st.markdown(content)
    st.markdown("---")

def get_ai_response(query: str) -> str:
    """Get AI response for genomics query."""
    # TODO: Implement AI response generation
    return f"Here's what I know about {query}..."

def render_chat_history() -> None:
    """Render chat history."""
    chat_history = get_state("chat_history", [])
    
    for message in chat_history:
        render_chat_message(message)

def render() -> None:
    """Render the AI assistant page."""
    st.title("Genomics AI Assistant")
    
    # Chat interface
    with st.container():
        st.markdown("### Ask me anything about genomics!")
        
        # Input
        user_input = st.text_input(
            "Your question",
            placeholder="e.g., What is a gene?",
            key="user_query",
        )
        
        # Process input
        if user_input:
            # Add user message to history
            chat_history = get_state("chat_history", [])
            chat_history.append(("user", user_input, "now"))
            
            # Get AI response
            response = get_ai_response(user_input)
            chat_history.append(("assistant", response, "now"))
            
            # Update state
            set_state("chat_history", chat_history)
            
            # Clear input
            st.session_state.user_query = ""
    
    # Display chat history
    render_chat_history()
    
    # Clear chat button
    if st.button("Clear Chat"):
        set_state("chat_history", []) 