"""
Fantasy Football Draft Assistant
A Streamlit application for analyzing QB statistics and making draft decisions.
"""
import streamlit as st
import plotly.express as px
from src.utils import load_qb_data, get_stat_ranges, filter_players

def main():
    st.title("Fantasy Football Draft Assistant 2024")
    st.write("Analyze QB statistics to make informed draft decisions")
    
    # Load data
    try:
        df = load_qb_data()
        stat_ranges = get_stat_ranges(df)
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return

    # Sidebar filters
    st.sidebar.header("Filter QBs by Stats")
    
    # Initialize filters dictionary
    filters = {}
    
    # Add filters for key stats
    key_stats = ['FPTS/G', 'TD', 'INT', 'YDS', 'CMP']
    for stat in key_stats:
        st.sidebar.subheader(f"{stat} Range")
        min_val = stat_ranges[stat]['min']
        max_val = stat_ranges[stat]['max']
        filters[stat] = {
            'min': st.sidebar.slider(f"Min {stat}", 
                                   min_value=float(min_val),
                                   max_value=float(max_val),
                                   value=float(min_val)),
            'max': st.sidebar.slider(f"Max {stat}", 
                                   min_value=float(min_val),
                                   max_value=float(max_val),
                                   value=float(max_val))
        }

    # Filter players based on criteria
    filtered_df = filter_players(df, filters)
    
    # Display results
    st.subheader("Filtered QB Rankings")
    st.dataframe(filtered_df.style.highlight_max(subset=['FPTS/G'], color='lightgreen'))
    
    # Visualizations
    st.subheader("QB Performance Analysis")
    
    # Points per Game vs Total TDs
    fig1 = px.scatter(filtered_df, 
                     x='TD', 
                     y='FPTS/G',
                     size='ROST',
                     hover_data=['Player'],
                     title='Points per Game vs Total TDs')
    st.plotly_chart(fig1)
    
    # Completion Percentage vs Yards
    fig2 = px.scatter(filtered_df,
                     x='PCT',
                     y='YDS',
                     size='FPTS/G',
                     hover_data=['Player'],
                     title='Completion Percentage vs Yards')
    st.plotly_chart(fig2)

if __name__ == "__main__":
    main()
