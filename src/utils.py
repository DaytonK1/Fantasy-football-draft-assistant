"""
Utility functions for Fantasy Football Draft Assistant.
This module contains data processing and analysis functions.
"""
import pandas as pd
import numpy as np

def load_qb_data():
    """
    Load and preprocess QB statistics data.
    
    Returns:
        pd.DataFrame: Processed QB statistics
    """
    df = pd.read_csv('data/qb_stats_2024.csv')
    # Clean player names to remove team
    df['Player'] = df['Player'].apply(lambda x: x.split(' (')[0])
    
    # Round float columns to 2 decimal places
    float_cols = df.select_dtypes(include=['float64']).columns
    df[float_cols] = df[float_cols].round(2)
    
    return df

def load_wr_data():
    """
    Load and preprocess WR statistics data.
    
    Returns:
        pd.DataFrame: Processed WR statistics
    """
    df = pd.read_csv('data/wr_stats_2024.csv')
    # Clean player names to remove team
    df['Player'] = df['Player'].apply(lambda x: x.split(' (')[0])
    
    # Convert string numbers with commas to float
    numeric_cols = ['YDS', 'REC', 'TGT', 'TD', 'ATT', 'FPTS', 'FPTS/G']
    for col in numeric_cols:
        df[col] = df[col].apply(lambda x: float(str(x).replace(',', '')))
    
    # Convert percentage to float
    df['ROST'] = df['ROST'].apply(lambda x: float(x.strip('%')))
    
    # Round float columns to 2 decimal places
    float_cols = df.select_dtypes(include=['float64']).columns
    df[float_cols] = df[float_cols].round(2)
    
    return df

def load_rb_data():
    """
    Load and preprocess RB statistics data.
    
    Returns:
        pd.DataFrame: Processed RB statistics
    """
    df = pd.read_csv('data/rb_stats_2024.csv')
    # Clean player names to remove team
    df['Player'] = df['Player'].apply(lambda x: x.split(' (')[0])
    
    # Rename receiving yards column to avoid confusion
    df = df.rename(columns={'YDS.1': 'REC_YDS', 'TD.1': 'REC_TD'})
    
    # Round float columns to 2 decimal places
    float_cols = df.select_dtypes(include=['float64']).columns
    df[float_cols] = df[float_cols].round(2)
    
    return df

def get_stat_ranges(df):
    """
    Get the min and max values for each numerical stat.
    
    Args:
        df (pd.DataFrame): QB statistics dataframe
    
    Returns:
        dict: Dictionary of stat ranges
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    ranges = {}
    for col in numeric_cols:
        ranges[col] = {
            'min': round(df[col].min(), 2),
            'max': round(df[col].max(), 2)
        }
    return ranges

def filter_players(df, filters):
    """
    Filter players based on stat criteria.
    
    Args:
        df (pd.DataFrame): QB statistics dataframe
        filters (dict): Dictionary of stat filters with min and max values
    
    Returns:
        pd.DataFrame: Filtered dataframe
    """
    filtered_df = df.copy()
    for stat, values in filters.items():
        if values.get('min') is not None:
            filtered_df = filtered_df[filtered_df[stat] >= values['min']]
        if values.get('max') is not None:
            filtered_df = filtered_df[filtered_df[stat] <= values['max']]
    return filtered_df
