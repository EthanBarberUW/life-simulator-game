from flask import Flask, jsonify, request
from flask_cors import CORS
from game_state_manager import GameStateManager
from datetime import datetime

app = Flask(__name__)
CORS(app, supports_credentials=True)

game_manager = GameStateManager()

@app.route('/api/new_game', methods=['POST'])
def new_game():
    data = request.json
    game_state = game_manager.new_game(
        character_name=data['name'],
        birthday=datetime.strptime(data['birthday'], '%Y-%m-%d').date(),
        job=data['job']
    )
    return jsonify({"message": "New game created", "character": game_state.character.__dict__})

@app.route('/api/progress_month', methods=['POST'])
def progress_month():
    events = game_manager.progress_month()
    return jsonify({
        "message": "Month progressed",
        "events": [event.__dict__ for event in events],
        "new_date": game_manager.game_state.current_date.isoformat()
    })

@app.route('/api/add_asset', methods=['POST'])
def add_asset():
    data = request.json
    game_manager.add_asset(name=data['name'], value=data['value'], asset_type=data['type'])
    return jsonify({"message": "Asset added", "net_worth": game_manager.get_net_worth()})

@app.route('/api/add_liability', methods=['POST'])
def add_liability():
    data = request.json
    game_manager.add_liability(name=data['name'], amount=data['amount'], liability_type=data['type'])
    return jsonify({"message": "Liability added", "net_worth": game_manager.get_net_worth()})

@app.route('/api/net_worth', methods=['GET'])
def get_net_worth():
    return jsonify({"net_worth": game_manager.get_net_worth()})

if __name__ == '__main__':
    app.run(debug=True)