import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [players, setPlayers] = useState([]);

    // Fetch data from Flask API
    useEffect(() => {
        axios.get('http://127.0.0.1:5000/players')
            .then(response => {
                setPlayers(response.data);
            })
            .catch(error => {
                console.error("There was an error fetching the data!", error);
            });
    }, []);

    return (
        <div className="App">
            <ul>
            {players.map((player) => (
                <li key={player.player_id}>
              <     strong>{player.web_name}</strong> | Team: {player.team} | Points:{" "}
                {player.total_points}
            </li>
                ))}
            </ul>

            <ul>
          
        </ul>
        </div>
    );
}

export default App;
