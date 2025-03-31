"""
Fantasy Football Draft Assistant 2025
A Streamlit application for analyzing 2024 NFL statistics to make informed draft decisions for 2025.
"""
import streamlit as st
import plotly.express as px
import pandas as pd
from src.utils import load_qb_data, load_wr_data, load_rb_data, get_stat_ranges, filter_players

def format_numbers(df):
    """Format numbers in the dataframe to display 2 decimal places"""
    float_cols = df.select_dtypes(include=['float64']).columns
    for col in float_cols:
        df[col] = df[col].apply(lambda x: f"{x:.2f}")
    return df

def create_stat_filters(stat_ranges, key_stats, position_prefix):
    """Create filters for stats with sliders"""
    filters = {}
    for stat in key_stats:
        st.sidebar.subheader(f"{stat} Range")
        min_val = stat_ranges[stat]['min']
        max_val = stat_ranges[stat]['max']
        filters[stat] = {
            'min': st.sidebar.slider(f"Min {stat}", 
                                   min_value=float(min_val),
                                   max_value=float(max_val),
                                   value=float(min_val),
                                   step=0.01,
                                   format="%.2f",
                                   key=f"{position_prefix}_{stat}_min"),
            'max': st.sidebar.slider(f"Max {stat}", 
                                   min_value=float(min_val),
                                   max_value=float(max_val),
                                   value=float(max_val),
                                   step=0.01,
                                   format="%.2f",
                                   key=f"{position_prefix}_{stat}_max")
        }
    return filters

def display_stats(position, load_func, key_stats):
    """Display statistics for a given position"""
    st.header(f"{position} Statistics")
    st.write(f"Analyze {position} statistics to make informed draft decisions")
    
    # Load data
    try:
        df = load_func()
        stat_ranges = get_stat_ranges(df)
    except Exception as e:
        st.error(f"Error loading {position} data: {str(e)}")
        return

    # Sidebar filters
    st.sidebar.header(f"Filter {position} by Stats")
    filters = create_stat_filters(stat_ranges, key_stats, position.lower()[:2])
    
    # Filter and format data
    filtered_df = filter_players(df, filters)
    display_df = format_numbers(filtered_df.copy())
    
    # Display results
    st.subheader(f"Filtered {position} Rankings")
    st.dataframe(display_df.style.highlight_max(subset=['FPTS/G'], color='lightgreen'))
    
    # Visualizations
    st.subheader(f"{position} Performance Visualization")
    plot_stat = st.selectbox("Select Stat to Plot", key_stats, key=f"{position.lower()[:2]}_plot_stat")
    fig = px.scatter(filtered_df, x=plot_stat, y='FPTS/G', 
                    hover_data=['Player'], title=f"{plot_stat} vs Fantasy Points per Game")
    st.plotly_chart(fig)

def main():
    st.title("Fantasy Football Draft Assistant 2025")
    st.write("Using 2024 NFL season statistics to help you make informed draft decisions")
    
    # Position configurations
    positions = {
        "Quarterbacks": {
            "load_func": load_qb_data,
            "key_stats": ['FPTS/G', 'TD', 'INT', 'YDS', 'CMP']
        },
        "Wide Receivers": {
            "load_func": load_wr_data,
            "key_stats": ['FPTS/G', 'REC', 'TGT', 'YDS', 'TD']
        },
        "Running Backs": {
            "load_func": load_rb_data,
            "key_stats": ['FPTS/G', 'YDS', 'TD', 'REC', 'REC_YDS', 'REC_TD']
        }
    }
    
    # Add navigation
    position = st.sidebar.radio("Select Position", list(positions.keys()))
    
    # Display selected position stats
    display_stats(position, 
                 positions[position]["load_func"],
                 positions[position]["key_stats"])

if __name__ == "__main__":
    main()
