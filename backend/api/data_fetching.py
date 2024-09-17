import requests
import psycopg2

# Fetch data from FPL API
response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")

# Check if the request was successful
if response.status_code == 200:
    print("API request successful!")
    data = response.json()
    # Print the first player's data to check the structure
    print(data['elements'][0])  # Prints the first player's data
else:
    print(f"API request failed with status code {response.status_code}")

data = response.json()

# Extract player information from the 'elements' field
players = data['elements']

# Example of detailed player data fields to extract
for player in players:
    player_info = {
        'id': player['id'],
        'first_name': player['first_name'],
        'second_name': player['second_name'],
        'team': player['team'],
        'position': player['element_type'],
        'total_points': player['total_points'],
        'now_cost': player['now_cost'],
        'minutes': player['minutes'],
        'goals_scored': player['goals_scored'],
        'assists': player['assists'],
        'clean_sheets': player['clean_sheets'],
        'yellow_cards': player['yellow_cards'],
        'red_cards': player['red_cards'],
        'saves': player['saves']
    }
    print(player_info)

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="FPL-ASSISTANT",
    user="fredericstrand",
    password="FPL",
    host="localhost"
)

# Create a cursor
cur = conn.cursor()

# Prepare the SQL query to insert player data
insert_query = """
    INSERT INTO players (id, first_name, second_name, team, position, total_points, now_cost, minutes, goals_scored, assists, clean_sheets, yellow_cards, red_cards, saves)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (id) DO NOTHING;
"""

# Loop through each player and insert their data into the database
for player in players:
    cur.execute(insert_query, (
        player['id'],
        player['first_name'],
        player['second_name'],
        player['team'],
        player['element_type'],
        player['total_points'],
        player['now_cost'],
        player['minutes'],
        player['goals_scored'],
        player['assists'],
        player['clean_sheets'],
        player['yellow_cards'],
        player['red_cards'],
        player['saves']
    ))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Table created successfully!")