# scripts/analysis.py
import pandas as pd

def team_stats(df, team_name):
    """Get win stats for a specific team."""
    team_matches = df[(df['Team1'] == team_name) | (df['Team2'] == team_name)]
    wins = len(team_matches[team_matches['Winner'] == team_name])
    total_matches = len(team_matches)
    win_percentage = (wins / total_matches) * 100
    return {
        'Total Matches': total_matches,
        'Wins': wins,
        'Win Percentage': round(win_percentage, 2)
    }

def top_performers(df, stat, top_n=5):
    """Get top players based on a specific stat (e.g., 'Runs', 'Wickets')."""
    return df.groupby('Player')[stat].sum().sort_values(ascending=False).head(top_n)