"""
Utility functions for Fantasy Football Draft Assistant.
This module contains data processing and analysis functions.
"""
import pandas as pd
import numpy as np

def clean_player_name(name):
    """Clean player name by removing team information"""
    return name.split(' (')[0]

def round_float_columns(df):
    """Round all float columns to 2 decimal places"""
    float_cols = df.select_dtypes(include=['float64']).columns
    return df.round({col: 2 for col in float_cols})

def load_data(file_path, column_renames=None):
    """
    Generic function to load and preprocess player statistics.
    
    Args:
        file_path (str): Path to the CSV file
        column_renames (dict, optional): Dictionary of column names to rename
    
    Returns:
        pd.DataFrame: Processed player statistics
    """
    df = pd.read_csv(file_path)
    df['Player'] = df['Player'].apply(clean_player_name)
    
    if column_renames:
        df = df.rename(columns=column_renames)
    
    return round_float_columns(df)

def load_qb_data():
    """Load and preprocess QB statistics"""
    return load_data('data/qb_stats_2024.csv')

def load_wr_data():
    """Load and preprocess WR statistics"""
    df = load_data('data/wr_stats_2024.csv')
    
    # Convert string numbers with commas to float
    numeric_cols = ['YDS', 'REC', 'TGT', 'TD', 'ATT', 'FPTS', 'FPTS/G']
    for col in numeric_cols:
        df[col] = df[col].apply(lambda x: float(str(x).replace(',', '')))
    
    # Convert percentage to float
    df['ROST'] = df['ROST'].apply(lambda x: float(x.strip('%')))
    
    return round_float_columns(df)

def load_rb_data():
    """Load and preprocess RB statistics"""
    return load_data('data/rb_stats_2024.csv', 
                    column_renames={'YDS.1': 'REC_YDS', 'TD.1': 'REC_TD'})

def get_stat_ranges(df):
    """Get the min and max values for each numerical stat"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    return {col: {'min': round(df[col].min(), 2),
                 'max': round(df[col].max(), 2)} 
            for col in numeric_cols}

def filter_players(df, filters):
    """Filter players based on stat criteria"""
    filtered_df = df.copy()
    for stat, values in filters.items():
        if values.get('min') is not None:
            filtered_df = filtered_df[filtered_df[stat] >= values['min']]
        if values.get('max') is not None:
            filtered_df = filtered_df[filtered_df[stat] <= values['max']]
    return filtered_df
