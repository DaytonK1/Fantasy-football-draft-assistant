"""
Data loading and processing utilities for the Fantasy Football Draft Assistant
"""
import pandas as pd
import numpy as np

def clean_player_name(name):
    """Remove team information from player name"""
    return name.split(' (')[0] if ' (' in name else name

def round_float_columns(df):
    """Round float columns to 2 decimal places"""
    float_cols = df.select_dtypes(include=['float64']).columns
    df[float_cols] = df[float_cols].round(2)
    return df

def load_data(file_path):
    """Load and preprocess data from a CSV file"""
    try:
        df = pd.read_csv(file_path)
        df['Player'] = df['Player'].apply(clean_player_name)
        
        # Convert percentage strings to floats
        if 'ROST' in df.columns:
            if df['ROST'].dtype == 'object':  # Only convert if it's a string
                df['ROST'] = df['ROST'].str.rstrip('%').astype(float) / 100
        
        # Convert string numbers to float
        for col in df.columns:
            if col not in ['Player', 'Team', 'Rank']:
                if df[col].dtype == 'object':  # Only convert if it's a string
                    df[col] = pd.to_numeric(df[col].str.replace(',', ''), errors='coerce')
        
        return df
    except Exception as e:
        raise Exception(f"Error loading data from {file_path}: {str(e)}")

def get_stat_ranges(df):
    """Get min and max values for each stat"""
    stat_ranges = {}
    for col in df.columns:
        if col not in ['Player', 'Team', 'Rank']:
            try:
                stat_ranges[col] = {
                    'min': float(df[col].min()),
                    'max': float(df[col].max())
                }
            except:
                continue
    return stat_ranges

def filter_players(df, filters):
    """Filter players based on stat ranges"""
    filtered_df = df.copy()
    for stat, ranges in filters.items():
        filtered_df = filtered_df[
            (filtered_df[stat] >= ranges['min']) & 
            (filtered_df[stat] <= ranges['max'])
        ]
    return filtered_df

def load_qb_data():
    """Load QB statistics"""
    return load_data('data/qb_stats_2024.csv')

def load_wr_data():
    """Load WR statistics"""
    return load_data('data/wr_stats_2024.csv')

def load_rb_data():
    """Load RB statistics"""
    return load_data('data/rb_stats_2024.csv')
