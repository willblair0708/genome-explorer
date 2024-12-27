"""Genomics simulation laboratory page."""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from typing import Dict, List

from genome_explorer.core import (
    MutationEvent,
    SimulationState,
    get_state,
    set_state,
)

def render_simulation_controls() -> Dict[str, float]:
    """Render simulation parameter controls."""
    st.sidebar.subheader("Simulation Parameters")
    
    params = get_state("simulation_params")
    
    mutation_rate = st.sidebar.slider(
        "Mutation Rate",
        min_value=0.0001,
        max_value=0.01,
        value=params["mutation_rate"],
        format="%.4f",
    )
    
    population_size = st.sidebar.slider(
        "Population Size",
        min_value=10,
        max_value=1000,
        value=params["population_size"],
    )
    
    generations = st.sidebar.slider(
        "Generations",
        min_value=1,
        max_value=100,
        value=params["generations"],
    )
    
    new_params = {
        "mutation_rate": mutation_rate,
        "population_size": population_size,
        "generations": generations,
    }
    set_state("simulation_params", new_params)
    
    return new_params

def run_simulation(params: Dict[str, float]) -> List[SimulationState]:
    """Run genomics simulation with given parameters."""
    # TODO: Implement actual simulation
    states = []
    for gen in range(params["generations"]):
        states.append(
            SimulationState(
                generation=gen,
                population_size=params["population_size"],
                mutation_events=[],
                fitness_scores={"avg": np.random.random()},
                timestamp=None,
            )
        )
    return states

def render_simulation_results(states: List[SimulationState]) -> None:
    """Render simulation results visualization."""
    st.subheader("Simulation Results")
    
    # Plot fitness over generations
    generations = [s.generation for s in states]
    fitness = [s.fitness_scores["avg"] for s in states]
    
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=generations,
            y=fitness,
            mode="lines+markers",
            name="Average Fitness",
        )
    )
    
    fig.update_layout(
        title="Population Fitness Over Time",
        xaxis_title="Generation",
        yaxis_title="Fitness Score",
        showlegend=True,
    )
    
    st.plotly_chart(fig, use_container_width=True)

def render() -> None:
    """Render the simulation laboratory page."""
    st.title("Genomics Simulation Lab")
    
    # Simulation controls
    params = render_simulation_controls()
    
    # Run simulation button
    if st.button("Run Simulation"):
        with st.spinner("Running simulation..."):
            states = run_simulation(params)
            set_state("simulation_results", states)
            st.success("Simulation complete!")
    
    # Display results
    results = get_state("simulation_results")
    if results:
        render_simulation_results(results) 