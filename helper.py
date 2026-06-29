# ==========================================
# IPL Cricket Analytics Dashboard
# File Name : helper.py
# Author : Gautam Jha
# ==========================================

# Import Required Libraries
import pandas as pd
import numpy as np

# -----------------------------
# Load Datasets
# -----------------------------

matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

# -----------------------------
# Display Basic Information
# -----------------------------

def show_basic_info():
    print("=" * 60)
    print("IPL ANALYTICS DASHBOARD")
    print("=" * 60)

    print("\nMatches Dataset Shape :", matches.shape)
    print("Deliveries Dataset Shape :", deliveries.shape)

    print("\nMatches Columns\n")
    print(matches.columns.tolist())

    print("\nDeliveries Columns\n")
    print(deliveries.columns.tolist())

# -----------------------------
# Missing Values
# -----------------------------

def check_missing_values():
    print("\nMissing Values (Matches)\n")
    print(matches.isnull().sum())

    print("\nMissing Values (Deliveries)\n")
    print(deliveries.isnull().sum())

# -----------------------------
# Duplicate Rows
# -----------------------------

def remove_duplicates():
    global matches, deliveries

    matches = matches.drop_duplicates()

    deliveries = deliveries.drop_duplicates()

    print("\nDuplicate Rows Removed Successfully")

# -----------------------------
# Dataset Information
# -----------------------------

def dataset_info():
    print("\nMatches Info\n")

    print(matches.info())

    print("\nDeliveries Info\n")

    print(deliveries.info())

# -----------------------------
# Team List
# -----------------------------

def get_teams():

    teams = sorted(matches['team1'].dropna().unique())

    return teams

# -----------------------------
# Season List
# -----------------------------

def get_seasons():

    seasons = sorted(matches['season'].dropna().unique())

    return seasons

# -----------------------------
# City List
# -----------------------------

def get_cities():

    cities = sorted(matches['city'].dropna().unique())

    return cities

# -----------------------------
# Venue List
# -----------------------------

def get_venues():

    venues = sorted(matches['venue'].dropna().unique())

    return venues

# -----------------------------
# Run File
# -----------------------------

if __name__ == "__main__":

    show_basic_info()

    check_missing_values()

    standardize_team_names()
    # -----------------------------
# Merge Datasets
# -----------------------------

def merge_dataset():

    merged_data = deliveries.merge(
        matches,
        left_on='match_id',
        right_on='id',
        how='left'
    )

    print("\nMerged Dataset Shape :", merged_data.shape)

    return merged_data

    remove_duplicates()
    # -----------------------------
# Standardize Team Names
# -----------------------------

def standardize_team_names():

    global matches, deliveries

    team_name_changes = {
        'Delhi Daredevils': 'Delhi Capitals',
        'Kings XI Punjab': 'Punjab Kings',
        'Rising Pune Supergiant': 'Rising Pune Supergiants'
    }

    matches.replace(team_name_changes, inplace=True)
    deliveries.replace(team_name_changes, inplace=True)

    print("\nTeam Names Standardized Successfully")
    merged_data = merge_dataset()

print("\nMerged Dataset Created Successfully")
dataset_info()
print("\nAvailable Teams")
print(get_teams())
print("\nAvailable Seasons")
print(get_seasons())
print("\nAvailable Cities")
print(get_cities())
print("\nAvailable Venues")
print(get_venues())
print("\nProject Started Successfully")