# dashboard/app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scripts.analysis import team_stats, top_performers

# Load processed data
@st.cache
def load_data():
    return pd.read_csv('data/processed_data.csv')

data = load_data()

# Dashboard title
st.title("🏏 T20 World Cup Data Analysis Dashboard")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a Section", ["Team Performance", "Player Analysis", "Trends"])

# Team Performance Section
if options == "Team Performance":
    st.header("Team Performance")
    team_name = st.selectbox("Select a Team", data['Team1'].unique())
    stats = team_stats(data, team_name)
    st.write(f"### {team_name} Stats")
    st.write(stats)

# Player Analysis Section
elif options == "Player Analysis":
    st.header("Top Players")
    stat_type = st.selectbox("Select Stat Type", ["Runs", "Wickets"])
    top_n = st.slider("Number of Players", min_value=1, max_value=10, value=5)
    top_players = top_performers(data, stat_type, top_n)
    st.write(f"### Top {top_n} Players by {stat_type}")
    st.table(top_players)

# Trends Section
elif options == "Trends":
    st.header("Performance Trends")
    team_name = st.selectbox("Select a Team for Trends", data['Team1'].unique())
    team_data = data[(data['Team1'] == team_name) | (data['Team2'] == team_name)]
    yearly_wins = team_data[team_data['Winner'] == team_name].groupby('Year').size()

    # Plot trends
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=yearly_wins.index, y=yearly_wins.values, marker='o')
    plt.title(f"{team_name} Yearly Win Trends")
    plt.xlabel("Year")
    plt.ylabel("Wins")
    st.pyplot(plt)