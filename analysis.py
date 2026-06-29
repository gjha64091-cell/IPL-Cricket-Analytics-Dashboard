import pandas as pd
import helper

# Data Load
matches = helper.matches
deliveries = helper.deliveries

# -----------------------------
# Total Matches
# -----------------------------
def total_matches():
    return matches.shape[0]

# -----------------------------
# Total Seasons
# -----------------------------
def total_seasons():
    return matches['season'].nunique()

# -----------------------------
# Total Teams
# -----------------------------
def total_teams():
    teams = pd.concat([matches['team1'], matches['team2']]).unique()
    return len(teams)

# -----------------------------
# Total Venues
# -----------------------------
def total_venues():
    return matches['venue'].nunique()

# -----------------------------
# Total Players
# -----------------------------
def total_players():
    return deliveries['batter'].nunique()

# -----------------------------
# Team Wins
# -----------------------------
def team_wins():
    return matches['winner'].value_counts()

# -----------------------------
# Top Run Scorers
# -----------------------------
def top_run_scorers():
    return deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)

# -----------------------------
# Top Wicket Takers
# -----------------------------
def top_wicket_takers():
    wickets = deliveries[deliveries['player_dismissed'].notna()]
    return wickets['bowler'].value_counts().head(10)

# -----------------------------
# Most Sixes
# -----------------------------
def most_sixes():
    sixes = deliveries[deliveries['batsman_runs'] == 6]
    return sixes['batter'].value_counts().head(10)

# -----------------------------
# Most Fours
# -----------------------------
def most_fours():
    fours = deliveries[deliveries['batsman_runs'] == 4]
    return fours['batter'].value_counts().head(10)

# -----------------------------
# Team Statistics
# -----------------------------
def team_stats(team_name):
    team_matches = matches[
        (matches['team1'] == team_name) |
        (matches['team2'] == team_name)
    ]

    total_matches = team_matches.shape[0]

    total_wins = team_matches[
        team_matches['winner'] == team_name
    ].shape[0]

    win_percentage = round(
        (total_wins / total_matches) * 100, 2
    )

    return {
        "Matches": total_matches,
        "Wins": total_wins,
        "Win %": win_percentage
    }

# -----------------------------
# Individual Player Runs
# -----------------------------
def player_runs(player_name):
    runs = deliveries[
        deliveries['batter'] == player_name
    ]['batsman_runs'].sum()
    return runs

# -----------------------------
# Orange Cap
# -----------------------------
def orange_cap():
    orange = deliveries.groupby("batter")["batsman_runs"].sum()
    orange = orange.sort_values(ascending=False).head(10)
    return orange

# -----------------------------
# Purple Cap
# -----------------------------
def purple_cap():
    wickets = deliveries[deliveries["player_dismissed"].notna()]
    purple = wickets["bowler"].value_counts().head(10)
    return purple

# -----------------------------
# Venue Analysis
# -----------------------------
def venue_matches():
    venue = matches["venue"].value_counts()
    return venue

# -----------------------------
# Venue Average Score
# -----------------------------
def venue_average_score():
    merged = deliveries.merge(
        matches,
        left_on="match_id",
        right_on="id"
    )
    avg = merged.groupby("venue")["total_runs"].mean()
    avg = avg.round(2)
    return avg.sort_values(ascending=False)

# ==========================================================
# New Analytics Functions (Added Successfully)
# ==========================================================

# 1. Total Unique Match Winners
def total_champions():
    return matches['winner'].dropna().nunique()

# 2. Season-wise total matches count
def season_wise_matches():
    return matches.groupby('season').size()

# 3. Top 10 venues where most matches played
def top_venues():
    return matches['venue'].value_counts().head(10)

# 4. Most successful team with maximum match wins
def most_successful_team():
    return matches['winner'].value_counts().head(1)

# 5. Dashboard aggregate statistics summary mapping
def dashboard_summary():
    return {
        "matches": total_matches(),
        "seasons": total_seasons(),
        "teams": total_teams(),
        "venues": total_venues(),
        "players": total_players()
    }


if __name__ == "__main__":
    print("--- Existing Analysis Main Outputs ---")
    print("Total Matches :", total_matches())
    print("Total Seasons :", total_seasons())
    print("Total Teams :", total_teams())
    print("Total Venues :", total_venues())
    print("Total Players :", total_players())

    print("\n--- Testing New Functions Output ---")
    print("Total Unique Match Winners (Champions Category):", total_champions())
    print("\nSeason Wise Matches:")
    print(season_wise_matches())
    print("\nTop 10 Venues:")
    print(top_venues())
    print("\nMost Successful Team:")
    print(most_successful_team())
    print("\nDashboard Aggregation Summary Dictionary:")
    print(dashboard_summary())