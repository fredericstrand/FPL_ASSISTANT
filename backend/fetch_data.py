import psycopg2
import requests
from collections import defaultdict

# Team strength data matching API team names
team_strengths = {
    'Manchester City': 5,
    'Arsenal': 5,
    'Liverpool': 4,
    'Chelsea': 4,
    'Tottenham': 3,
    'Manchester United': 3,
    'Aston Villa': 3,
    'Newcastle': 3,
    'Brighton': 3,
    'West Ham': 3,
    'Crystal Palace': 2,
    'Brentford': 2,
    'Wolves': 2,
    'Fulham': 2,
    'Everton': 2,
    'Bournemouth': 2,
    "Nott'm Forest": 1,
    'Southampton': 1,
    'Leicester': 1,
    'Ipswich': 1
}

# Fetch player and team data from the Fantasy Premier League API
def fetch_player_data():
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    response = requests.get(url)
    data = response.json()
    return data['elements'], data['teams']

players, teams = fetch_player_data()

# Map team IDs to team names
team_id_to_name = {team['id']: team['name'] for team in teams}

# Fetch upcoming fixtures data from the Fantasy Premier League API
def fetch_upcoming_fixtures():
    url = "https://fantasy.premierleague.com/api/fixtures/"
    response = requests.get(url)
    fixtures = response.json()
    return fixtures

upcoming_fixtures = fetch_upcoming_fixtures()

# Create opponents dictionary, mapping teams to their upcoming opponents
def get_opponents(fixtures):
    team_opponents = defaultdict(list)
    for fixture in fixtures:
        home_team = fixture['team_h']
        away_team = fixture['team_a']
        team_opponents[home_team].append(away_team)
        team_opponents[away_team].append(home_team)

    # Restrict to the next 3 opponents
    for team in team_opponents:
        team_opponents[team] = team_opponents[team][:3]
    return team_opponents

opponents_dict = get_opponents(upcoming_fixtures)

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="fredericstrand", 
    user="fredericstrand", 
    password="FPL", 
    host="localhost", 
    port="5432"
)
cursor = conn.cursor()

# Insert player stats into the PostgreSQL table
insert_query = """
INSERT INTO player_stats (
    player_id, web_name, first_name, second_name, team, team_code, status,
    chance_of_playing_next_round, chance_of_playing_this_round, now_cost, total_points, 
    event_points, form, points_per_game, selected_by_percent, transfers_in, transfers_out,
    goals_scored, assists, clean_sheets, goals_conceded, yellow_cards, red_cards, saves,
    bonus, bps, influence, creativity, threat, ict_index, expected_goals, expected_assists, 
    expected_goal_involvements, expected_goals_conceded, next_opponent_1, next_opponent_2, next_opponent_3, difficulty_rating
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

# Calculate player stats including team difficulty ratings
for player in players:
    team_id = player["team"]
    team_name = team_id_to_name[team_id]  # Get team name from team ID
    next_opponents = opponents_dict.get(team_id, [])  # Get upcoming opponent team IDs
    
    # Map opponent team IDs
    opponent_team_names = [team_id_to_name[opponent] for opponent in next_opponents]
    next_opponent_1, next_opponent_2, next_opponent_3 = opponent_team_names
    
    # Calculate the average difficulty rating
    opponent_team_ratings = [team_strengths.get(opponent, 0) for opponent in opponent_team_names]
    difficulty_rating = sum(opponent_team_ratings) / len(opponent_team_ratings) if opponent_team_ratings else 0
    
    

    # Prepare the data for insertion
    player_data = (
        player.get('id'), 
        player.get('web_name', ''),
        player.get('first_name', ''),
        player.get('second_name', ''),
        player.get('team'),
        player.get('team_code'),
        player.get('status', ''),
        player.get('chance_of_playing_next_round', 0),
        player.get('chance_of_playing_this_round', 0),
        player.get('now_cost', 0), 
        player.get('total_points', 0), 
        player.get('event_points', 0), 
        player.get('form', '0.0'), 
        player.get('points_per_game', 0), 
        player.get('selected_by_percent', 0), 
        player.get('transfers_in', 0), 
        player.get('transfers_out', 0), 
        player.get('goals_scored', 0), 
        player.get('assists', 0), 
        player.get('clean_sheets', 0), 
        player.get('goals_conceded', 0), 
        player.get('yellow_cards', 0), 
        player.get('red_cards', 0), 
        player.get('saves', 0), 
        player.get('bonus', 0), 
        player.get('bps', 0), 
        player.get('influence', 0), 
        player.get('creativity', 0), 
        player.get('threat', 0), 
        player.get('ict_index'), 
        player.get('expected_goals', 0), 
        player.get('expected_assists', 0), 
        player.get('expected_goal_involvements', 0), 
        player.get('expected_goals_conceded', 0),
        next_opponent_1, next_opponent_2, next_opponent_3,
        difficulty_rating
    )
    
    # Debugging: Print the data before executing the query
    query_debug = cursor.mogrify(insert_query, player_data)
    print("Executing SQL:\n", query_debug.decode('utf-8'))  # Decode to print it in a readable format


    # Insert data into the table
    cursor.execute(insert_query, player_data)

# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()

print("Data inserted into PostgreSQL successfully!")
