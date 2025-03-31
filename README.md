# Fantasy Football Draft Assistant 2025

## Project Overview
A Streamlit-based web application designed to help fantasy football managers make informed decisions during their 2025 season drafts. The application provides interactive filtering and visualization of player statistics from the 2024 NFL season to help predict performance for 2025.

## Features
- Filter QBs by key statistics (Points per Game, TDs, INTs, Yards, Completions)
- Filter WRs by key statistics (Points per Game, Receptions, Targets, Yards, TDs)
- Filter RBs by key statistics (Points per Game, Rushing Yards, Rushing TDs, Receptions, Receiving Yards, Receiving TDs)
- Interactive data visualization using Plotly
- Sortable statistics table with highlighting
- Player performance comparisons
- Roster percentage insights

## Installation
1. Clone this repository:
```bash
git clone https://github.com/DaytonK1/fantasy-football-draft-assistant.git
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
To run the Fantasy Football Draft Assistant:
```bash
streamlit run app.py
```

## Project Structure
```
streamlit-midterm/
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
├── data/              # Data directory
│   ├── qb_stats_2024.csv  # QB statistics from 2024 season
│   ├── wr_stats_2024.csv  # WR statistics from 2024 season
│   └── rb_stats_2024.csv  # RB statistics from 2024 season
└── src/               # Source code directory
    └── utils.py       # Data processing utilities
```

## Data Sources
- Player statistics from the 2024 NFL season used to inform 2025 draft decisions
- Includes passing, rushing, and receiving statistics
- Fantasy points calculated using standard scoring

## Development
This project follows standard Python coding and uses Git for version control.

## License
MIT License
