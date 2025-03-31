"""
Fantasy Football Draft Assistant
A Streamlit application for analyzing QB and WR statistics and making draft decisions.
"""
import streamlit as st
import plotly.express as px
from src.utils import load_qb_data, load_wr_data, get_stat_ranges, filter_players

def display_qb_stats():
    st.header("Quarterback Statistics")
    st.write("Analyze QB statistics to make informed draft decisions")
    
    # Load data
    try:
        df = load_qb_data()
        stat_ranges = get_stat_ranges(df)
    except Exception as e:
        st.error(f"Error loading QB data: {str(e)}")
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
                                   value=float(min_val),
                                   key=f"qb_{stat}_min"),
            'max': st.sidebar.slider(f"Max {stat}", 
                                   min_value=float(min_val),
                                   max_value=float(max_val),
                                   value=float(max_val),
                                   key=f"qb_{stat}_max")
        }

    # Filter players based on criteria
    filtered_df = filter_players(df, filters)
    
    # Display results
    st.subheader("Filtered QB Rankings")
    st.dataframe(filtered_df.style.highlight_max(subset=['FPTS/G'], color='lightgreen'))
    
    # Visualizations
    st.subheader("QB Performance Visualization")
    plot_stat = st.selectbox("Select Stat to Plot", key_stats, key="qb_plot_stat")
    fig = px.scatter(filtered_df, x=plot_stat, y='FPTS/G', 
                    hover_data=['Player'], title=f"{plot_stat} vs Fantasy Points per Game")
    st.plotly_chart(fig)

def display_wr_stats():
    st.header("Wide Receiver Statistics")
    st.write("Analyze WR statistics to make informed draft decisions")
    
    # Load data
    try:
        df = load_wr_data()
        stat_ranges = get_stat_ranges(df)
    except Exception as e:
        st.error(f"Error loading WR data: {str(e)}")
        return

    # Sidebar filters
    st.sidebar.header("Filter WRs by Stats")
    
    # Initialize filters dictionary
    filters = {}
    
    # Add filters for key stats
    key_stats = ['FPTS/G', 'REC', 'TGT', 'YDS', 'TD']
    for stat in key_stats:
        st.sidebar.subheader(f"{stat} Range")
        min_val = stat_ranges[stat]['min']
        max_val = stat_ranges[stat]['max']
        filters[stat] = {
            'min': st.sidebar.slider(f"Min {stat}", 
                                   min_value=float(min_val),
                                   max_value=float(max_val),
                                   value=float(min_val),
                                   key=f"wr_{stat}_min"),
            'max': st.sidebar.slider(f"Max {stat}", 
                                   min_value=float(min_val),
                                   max_value=float(max_val),
                                   value=float(max_val),
                                   key=f"wr_{stat}_max")
        }

    # Filter players based on criteria
    filtered_df = filter_players(df, filters)
    
    # Display results
    st.subheader("Filtered WR Rankings")
    st.dataframe(filtered_df.style.highlight_max(subset=['FPTS/G'], color='lightgreen'))
    
    # Visualizations
    st.subheader("WR Performance Visualization")
    plot_stat = st.selectbox("Select Stat to Plot", key_stats, key="wr_plot_stat")
    fig = px.scatter(filtered_df, x=plot_stat, y='FPTS/G', 
                    hover_data=['Player'], title=f"{plot_stat} vs Fantasy Points per Game")
    st.plotly_chart(fig)

def main():
    st.title("Fantasy Football Draft Assistant 2024")
    
    # Add navigation
    page = st.sidebar.radio("Select Position", ["Quarterbacks", "Wide Receivers"])
    
    if page == "Quarterbacks":
        display_qb_stats()
    else:
        display_wr_stats()

if __name__ == "__main__":
    main()
