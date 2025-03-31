# Fantasy Football Draft Assistant 2024

## Project Overview
A Streamlit-based web application designed to help fantasy football managers make informed decisions during their drafts. The application provides interactive filtering and visualization of QB statistics from the 2024 season.

## Features
- Filter QBs by key statistics (Points per Game, TDs, INTs, Yards, Completions)
- Interactive data visualization using Plotly
- Sortable statistics table with highlighting
- Player performance comparisons
- Roster percentage insights

## Installation
1. Clone this repository:
```bash
git clone [your-repo-url]
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
│   └── qb_stats_2024.csv  # QB statistics dataset
└── src/               # Source code directory
    └── utils.py       # Data processing utilities
```

## Data Sources
- QB statistics from 2024 NFL season
- Includes passing and rushing statistics
- Fantasy points calculated using standard scoring

## Development
This project follows standard Python coding conventions (PEP 8) and uses Git for version control.

## License
MIT License
