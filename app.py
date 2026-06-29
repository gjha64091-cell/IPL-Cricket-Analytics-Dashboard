import streamlit as st
import analysis
import helper
import pandas as pd
import plotly.express as px

# ==========================================
# Page Configuration
# ==========================================
st.set_page_config(
    page_title="IPL Cricket Analytics Dashboard",
    page_icon="🏏",
    layout="wide"
)

# ==========================================
# Custom CSS Loading
# ==========================================
def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# CSS file ko execute/load karna
load_css()

# ==========================================
# Sidebar Navigation
# ==========================================
st.sidebar.title("🏏 IPL Analytics")

page = st.sidebar.radio(
    "Select Analysis",
    [
        "Dashboard",
        "Team Analysis",
        "Player Analysis",
        "Venue Analysis",
        "Orange Cap",
        "Purple Cap"
    ]
)

st.sidebar.write("---")
st.sidebar.info("Developed by Gautam Jha")

# ==========================================
# 1. Dashboard Page (Updated with Summary & Overview Charts)
# ==========================================
if page == "Dashboard":
    st.title("🏏 IPL Cricket Analytics Dashboard")
    st.markdown("### Data Analysis using Python | Pandas | Streamlit")
    st.write("---")

    # Fetching aggregate dictionary data from analysis.py
    summary = analysis.dashboard_summary()

    # Dashboard KPI Cards using mapping values
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("🏏 Matches", summary["matches"])
    col2.metric("📅 Seasons", summary["seasons"])
    col3.metric("👥 Teams", summary["teams"])
    col4.metric("🏟 Venues", summary["venues"])
    col5.metric("👤 Players", summary["players"])

    st.write("---")
    
    # 1. Season wise trend line chart
    st.subheader("📅 Season Wise Matches")
    season = analysis.season_wise_matches()
    st.line_chart(season)
    
    # 2. Team overall wins distribution bar chart
    st.subheader("🏆 Team Winning Analysis")
    wins = analysis.team_wins()
    st.bar_chart(wins)
    
    # 3. Top stadiums bar chart
    st.subheader("🏟 Top IPL Venues")
    venue = analysis.top_venues()
    st.bar_chart(venue)
    
    st.write("---")
    
    # Grid layout for quick preview of Orange and Purple Cap
    col_orange, col_purple = st.columns(2)
    
    with col_orange:
        st.subheader("🟠 Orange Cap (Top Run Scorers)")
        orange = analysis.orange_cap()
        st.dataframe(orange, use_container_width=True)
        
    with col_purple:
        st.subheader("🟣 Purple Cap (Top Wicket Takers)")
        purple = analysis.purple_cap()
        st.dataframe(purple, use_container_width=True)
        
    st.success("Dashboard Loaded Successfully ✅")

# ==========================================
# 2. Team Analysis Page
# ==========================================
elif page == "Team Analysis":
    st.title("🏆 Team Analysis")
    st.write("---")

    # Dropdown for selecting a single team
    teams = sorted(list(set(helper.matches['team1'])))
    selected_team = st.selectbox(
        "Select Team",
        teams
    )

    # Individual Team Stats KPI
    stats = analysis.team_stats(selected_team)
    col1, col2, col3 = st.columns(3)
    col1.metric("Matches Played", stats["Matches"])
    col2.metric("Wins", stats["Wins"])
    col3.metric("Win %", stats["Win %"])

    st.write("---")

    # Plotly Bar Chart for Overall Team Wins
    st.subheader("📊 Overall Team Winning Records")
    team_win = analysis.team_wins()
    
    # Resetting index to convert series to dataframe for Plotly Express
    team_win_df = team_win.reset_index()
    team_win_df.columns = ["Team", "Wins"]

    # Creating interactive Plotly chart
    fig = px.bar(
        team_win_df,
        x="Team",
        y="Wins",
        title="IPL Team Wins",
        color="Wins",
        text_auto=True
    )

    # Displaying the chart in full width
    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================
# 3. Player Analysis Page
# ==========================================
elif page == "Player Analysis":
    st.title("🏏 Player Analysis")
    st.write("---")

    # Individual Player Statistics Dropdown
    st.subheader("🔍 Search Individual Player Stats")
    
    deliveries = helper.deliveries
    players_list = sorted(deliveries['batter'].dropna().unique())
    
    selected_player = st.selectbox(
        "Select Player",
        players_list
    )

    # Fetch and show runs for selected player
    runs = analysis.player_runs(selected_player)
    
    st.metric(
        label=f"📊 {selected_player}'s Career Runs",
        value=f"{runs:,}"
    )

    st.write("---")

    # Overall Top Lists Graphs
    st.subheader("🔥 Top 10 Run Scorers")
    st.bar_chart(analysis.top_run_scorers())

    st.subheader("🎯 Top 10 Wicket Takers")
    st.bar_chart(analysis.top_wicket_takers())

    st.subheader("💥 Most Sixes")
    st.bar_chart(analysis.most_sixes())

    st.subheader("⭐ Most Fours")
    st.bar_chart(analysis.most_fours())

# ==========================================
# 4. Venue Analysis Page
# ==========================================
elif page == "Venue Analysis":
    st.title("🏟 Venue Analysis")
    st.write("---")

    st.subheader("Matches Played")
    venue = analysis.venue_matches()
    st.bar_chart(venue)

    st.write("---")

    st.subheader("Average Runs")
    avg = analysis.venue_average_score()
    st.bar_chart(avg)

# ==========================================
# 5. Orange Cap Page
# ==========================================
elif page == "Orange Cap":
    st.title("🟠 Orange Cap")
    st.write("---")

    orange = analysis.orange_cap()
    st.bar_chart(orange)
    st.dataframe(orange)

# ==========================================
# 6. Purple Cap Page
# ==========================================
elif page == "Purple Cap":
    st.title("🟣 Purple Cap")
    st.write("---")

    purple = analysis.purple_cap()
    st.bar_chart(purple)
    st.dataframe(purple)