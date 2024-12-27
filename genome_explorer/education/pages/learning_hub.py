"""Educational content and learning hub page."""

import streamlit as st
from typing import Dict, List, Optional

from genome_explorer.core import (
    EducationModule,
    get_state,
    set_state,
)

SAMPLE_MODULES = [
    EducationModule(
        id="intro-dna",
        title="Introduction to DNA",
        description="Learn about the basic structure and function of DNA.",
        difficulty="Beginner",
        prerequisites=[],
        content="DNA (deoxyribonucleic acid) is the molecule that carries genetic information...",
        quiz={
            "q1": {
                "question": "What does DNA stand for?",
                "options": ["Deoxyribonucleic acid", "Diribonucleic acid", "Deoxyribose acid"],
                "correct": 0,
            }
        },
    ),
    EducationModule(
        id="mutations",
        title="Genetic Mutations",
        description="Understand different types of mutations and their effects.",
        difficulty="Intermediate",
        prerequisites=["intro-dna"],
        content="A genetic mutation is a permanent change in DNA sequence...",
        quiz={
            "q1": {
                "question": "What is a point mutation?",
                "options": ["Single base change", "Base deletion", "Base insertion"],
                "correct": 0,
            }
        },
    ),
]

def render_module_list() -> Optional[str]:
    """Render list of educational modules."""
    st.sidebar.subheader("Modules")
    
    selected = st.sidebar.radio(
        "Select Module",
        options=[m.title for m in SAMPLE_MODULES],
        index=0,
    )
    
    return next(m for m in SAMPLE_MODULES if m.title == selected)

def render_module_content(module: EducationModule) -> None:
    """Render module content."""
    st.header(module.title)
    st.markdown(f"**Difficulty:** {module.difficulty}")
    
    if module.prerequisites:
        st.markdown("**Prerequisites:** " + ", ".join(module.prerequisites))
    
    st.markdown("---")
    st.markdown(module.content)

def render_module_quiz(module: EducationModule) -> None:
    """Render module quiz."""
    st.subheader("Knowledge Check")
    
    correct_answers = 0
    total_questions = len(module.quiz)
    
    for qid, quiz in module.quiz.items():
        answer = st.radio(
            quiz["question"],
            options=quiz["options"],
            key=f"quiz_{module.id}_{qid}",
        )
        
        if st.button(f"Check Answer {qid}"):
            if quiz["options"].index(answer) == quiz["correct"]:
                st.success("Correct! 🎉")
                correct_answers += 1
            else:
                st.error("Try again!")
    
    if correct_answers == total_questions:
        if not module.completed:
            module.completed = True
            module.score = 100.0
            st.balloons()

def render() -> None:
    """Render the learning hub page."""
    st.title("Genomics Learning Hub")
    
    # Module selection
    selected_module = render_module_list()
    
    # Module content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        render_module_content(selected_module)
    
    with col2:
        render_module_quiz(selected_module)
    
    # Progress tracking
    st.sidebar.markdown("---")
    st.sidebar.subheader("Your Progress")
    completed = sum(1 for m in SAMPLE_MODULES if m.completed)
    st.sidebar.progress(completed / len(SAMPLE_MODULES)) 