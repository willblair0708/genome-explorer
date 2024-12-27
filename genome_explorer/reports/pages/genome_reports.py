"""Genome analysis reports page."""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from typing import Dict, List, Optional

from genome_explorer.core import (
    GenomeFeature,
    get_state,
    set_state,
)

def render_report_options() -> Dict[str, bool]:
    """Render report configuration options."""
    st.sidebar.subheader("Report Options")
    
    options = {
        "include_variants": st.sidebar.checkbox("Include Variants", value=True),
        "include_genes": st.sidebar.checkbox("Include Genes", value=True),
        "include_stats": st.sidebar.checkbox("Include Statistics", value=True),
        "include_viz": st.sidebar.checkbox("Include Visualizations", value=True),
    }
    
    return options

def generate_report(genome_file: str, options: Dict[str, bool]) -> Dict:
    """Generate genome analysis report."""
    # TODO: Implement actual report generation
    return {
        "summary": {
            "total_genes": 1000,
            "total_variants": 50,
            "gc_content": 0.42,
        },
        "features": [
            GenomeFeature(
                id="gene1",
                type="gene",
                region=None,
                attributes={"name": "Example"},
            )
        ],
    }

def render_report_summary(report: Dict) -> None:
    """Render report summary section."""
    st.subheader("Genome Summary")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Genes", report["summary"]["total_genes"])
    
    with col2:
        st.metric("Total Variants", report["summary"]["total_variants"])
    
    with col3:
        st.metric("GC Content", f"{report['summary']['gc_content']:.2%}")

def render_feature_table(features: List[GenomeFeature]) -> None:
    """Render feature table."""
    st.subheader("Genomic Features")
    
    # Convert features to dataframe
    df = pd.DataFrame([
        {
            "ID": f.id,
            "Type": f.type,
            "Name": f.attributes.get("name", ""),
        }
        for f in features
    ])
    
    st.dataframe(df)

def render() -> None:
    """Render the genome reports page."""
    st.title("Genome Analysis Reports")
    
    # Get current genome
    current_genome = get_state("current_genome")
    
    if not current_genome:
        st.warning("Please upload a genome file in the Visualizer first!")
        return
    
    # Report options
    options = render_report_options()
    
    # Generate report button
    if st.button("Generate Report"):
        with st.spinner("Generating report..."):
            report = generate_report(current_genome, options)
            set_state("current_report", report)
            st.success("Report generated!")
    
    # Display report
    report = get_state("current_report")
    if report:
        render_report_summary(report)
        if options["include_genes"]:
            render_feature_table(report["features"]) 