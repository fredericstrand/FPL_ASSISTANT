from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
CORS(app)

# PostgreSQL connection setup
conn = psycopg2.connect(
    dbname="fredericstrand",
    user="fredericstrand",
    password="FPL",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# API endpoint for fetching players
@app.route('/players', methods=['GET'])
def get_players():
    cursor.execute("SELECT * FROM player_stats LIMIT 10;")
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    result = [dict(zip(column_names, row)) for row in rows]
    return jsonify(result)

# Route to serve React's static files (for any path)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
